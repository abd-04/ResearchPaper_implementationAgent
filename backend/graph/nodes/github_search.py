from backend.tools.github_tool import search_github_repos


def github_search_node(state):

    print("\n--- GITHUB SEARCH NODE ---")

    title = state.get("extracted_title")

    if not title:
        title = state["paper_title"]

    query = f"{title} implementation pytorch"

    print("\nQUERY USED:\n")
    print(query)

    repos = search_github_repos(query)

    # -------- FALLBACK SEARCH -------- #

    if not repos:

        print("\nPRIMARY SEARCH FAILED")
        print("TRYING FALLBACK SEARCH...\n")

        fallback_query = f"{title} pytorch"

        repos = search_github_repos(fallback_query)

    print("\nREPOS FOUND:\n")
    print(repos)

    return {
        "github_repos": repos,
        "current_step": "github_search_completed"
    }