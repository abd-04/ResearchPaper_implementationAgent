import os


def packager_node(state):

    print("\n--- PACKAGER NODE ---")

    # -------- TEMP OUTPUT FOLDER -------- #

    output_dir = os.path.join(
        "outputs",
        "temp_output"
    )

    os.makedirs(output_dir, exist_ok=True)

    implementation_path = os.path.join(
        output_dir,
        "implementation.py"
    )

    summary_path = os.path.join(
        output_dir,
        "paper_summary.md"
    )

    explanation_path = os.path.join(
        output_dir,
        "explanation.md"
    )

    references_path = os.path.join(
        output_dir,
        "references.md"
    )

    # -------- SAVE IMPLEMENTATION -------- #

    with open(implementation_path, "w", encoding="utf-8") as f:
        f.write(state["generated_code"])

    # -------- SAVE SUMMARY -------- #

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(state["paper_summary"])

    # -------- SAVE EXPLANATION -------- #

    with open(explanation_path, "w", encoding="utf-8") as f:
        f.write(state["explanation"])

    # -------- SAVE REFERENCES -------- #

    with open(references_path, "w", encoding="utf-8") as f:

        repos = state.get("github_repos", [])

        if not repos:

            f.write("# No GitHub repositories found.\n")

        else:

            for repo in repos:

                f.write(f"## {repo['name']}\n\n")

                f.write(f"**Stars:** {repo['stars']}\n\n")

                f.write(
                    f"**Description:** "
                    f"{repo['description']}\n\n"
                )

                f.write(
                    f"[Open Repository]"
                    f"({repo['url']})\n\n"
                )

                f.write("---\n\n")

    return {

        "output_package": {
            "folder": output_dir
        },

        "current_step": "completed"
    }