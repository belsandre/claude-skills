#!/usr/bin/env python3
"""
Research State Manager for Company Research Skill

This script manages the state of ongoing research projects, allowing for
resumability when context limits are reached or research is interrupted.

Usage:
    python research_state.py init <project-name>
    python research_state.py add-source <project-name> <source-type> <source-name> <url>
    python research_state.py mark-complete <project-name> <source-type> <source-name>
    python research_state.py status <project-name>
    python research_state.py next-tasks <project-name>
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path


class ResearchState:
    """Manages the state of a research project."""

    def __init__(self, project_name):
        self.project_name = project_name
        self.state_file = self._get_state_file()
        self.state = self._load_state()

    @staticmethod
    def _get_outputs_base_dir():
        """
        Determine the base outputs directory.

        Priority:
        1. Environment variable RESEARCH_OUTPUTS_DIR if set
        2. Check if cwd contains 'users/{username}/' pattern -> use users/{username}/outputs
        3. Fall back to 'outputs' (standalone mode)

        Returns:
            Path: Base directory for research outputs
        """
        # Check environment variable first
        env_outputs = os.getenv('RESEARCH_OUTPUTS_DIR')
        if env_outputs:
            return Path(env_outputs)

        # Detect user context from current working directory
        cwd = Path.cwd()
        cwd_parts = cwd.parts

        # Look for 'users/{username}' pattern in path
        try:
            users_idx = cwd_parts.index('users')
            if users_idx + 1 < len(cwd_parts):
                username = cwd_parts[users_idx + 1]
                # Construct path to user's outputs directory
                users_root = Path(*cwd_parts[:users_idx + 2])  # /path/to/users/{username}
                return users_root / "outputs"
        except (ValueError, IndexError):
            pass

        # Fall back to standalone mode
        return Path("outputs")

    def _get_state_file(self):
        """Get the path to the state file for this project."""
        # Get the appropriate outputs directory
        outputs_dir = self._get_outputs_base_dir()

        # Search for project directory
        if outputs_dir.exists():
            for project_dir in outputs_dir.iterdir():
                if project_dir.is_dir() and self.project_name in project_dir.name:
                    state_file = project_dir / ".research_state.json"
                    return state_file

        # If not found, create new state file in current directory
        return Path(f".research_state_{self.project_name}.json")

    def _load_state(self):
        """Load state from file or create new state."""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {
            "project_name": self.project_name,
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "research_plan": [],
            "company_sources": {},
            "people_sources": {},
            "completed_sources": [],
            "notes": []
        }

    def _save_state(self):
        """Save state to file."""
        self.state["last_updated"] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
        print(f"State saved to: {self.state_file}")

    def init_project(self):
        """Initialize a new research project."""
        if self.state_file.exists():
            print(f"Project '{self.project_name}' already exists.")
            print(f"State file: {self.state_file}")
        else:
            self._save_state()
            print(f"Initialized new research project: {self.project_name}")
            print(f"State file: {self.state_file}")

    def add_source(self, source_type, source_name, url):
        """Add a source to the research plan."""
        if source_type == "company":
            self.state["company_sources"][source_name] = {
                "url": url,
                "status": "pending",
                "added_at": datetime.now().isoformat()
            }
        elif source_type == "people":
            self.state["people_sources"][source_name] = {
                "url": url,
                "status": "pending",
                "added_at": datetime.now().isoformat()
            }
        else:
            print(f"Invalid source type: {source_type}. Use 'company' or 'people'.")
            return

        self._save_state()
        print(f"Added {source_type} source: {source_name}")

    def mark_complete(self, source_type, source_name):
        """Mark a source as completed."""
        sources = self.state.get(f"{source_type}_sources", {})

        if source_name in sources:
            sources[source_name]["status"] = "completed"
            sources[source_name]["completed_at"] = datetime.now().isoformat()

            if source_name not in self.state["completed_sources"]:
                self.state["completed_sources"].append(source_name)

            self._save_state()
            print(f"Marked {source_type} source '{source_name}' as completed.")
        else:
            print(f"Source '{source_name}' not found in {source_type} sources.")

    def get_status(self):
        """Get the current status of the research project."""
        company_total = len(self.state["company_sources"])
        company_done = sum(1 for s in self.state["company_sources"].values() if s["status"] == "completed")

        people_total = len(self.state["people_sources"])
        people_done = sum(1 for s in self.state["people_sources"].values() if s["status"] == "completed")

        print(f"\nResearch Project: {self.project_name}")
        print(f"Created: {self.state['created_at']}")
        print(f"Last Updated: {self.state['last_updated']}")
        print(f"\nProgress:")
        print(f"  Company Sources: {company_done}/{company_total} completed")
        print(f"  People Sources: {people_done}/{people_total} completed")
        print(f"  Total Completed: {len(self.state['completed_sources'])}")

        return self.state

    def get_next_tasks(self):
        """Get the next pending tasks."""
        pending = []

        for name, info in self.state["company_sources"].items():
            if info["status"] == "pending":
                pending.append(("company", name, info["url"]))

        for name, info in self.state["people_sources"].items():
            if info["status"] == "pending":
                pending.append(("people", name, info["url"]))

        if pending:
            print(f"\nNext tasks ({len(pending)} remaining):")
            for i, (source_type, name, url) in enumerate(pending[:5], 1):
                print(f"  {i}. [{source_type}] {name}")
                print(f"     URL: {url}")
        else:
            print("\nNo pending tasks! Research is complete.")

        return pending


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    project_name = sys.argv[2]

    state = ResearchState(project_name)

    if command == "init":
        state.init_project()

    elif command == "add-source":
        if len(sys.argv) < 6:
            print("Usage: research_state.py add-source <project-name> <source-type> <source-name> <url>")
            sys.exit(1)
        source_type = sys.argv[3]
        source_name = sys.argv[4]
        url = sys.argv[5]
        state.add_source(source_type, source_name, url)

    elif command == "mark-complete":
        if len(sys.argv) < 5:
            print("Usage: research_state.py mark-complete <project-name> <source-type> <source-name>")
            sys.exit(1)
        source_type = sys.argv[3]
        source_name = sys.argv[4]
        state.mark_complete(source_type, source_name)

    elif command == "status":
        state.get_status()

    elif command == "next-tasks":
        state.get_next_tasks()

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
