#!/usr/bin/env python3
"""
OpenClaw Resource Repository Updater

Searches for new resources about OpenClaw across various platforms
and updates the repository with findings.

Usage:
    python update_resources.py

Requirements:
    pip install requests beautifulsoup4
"""

import os
import json
import requests
from datetime import datetime

# Configuration
SEARCH_TERMS = ["openclaw", "moltbot", "clawdbot"]
OUTPUT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def search_hacker_news(query: str) -> list:
    """Search Hacker News for posts about OpenClaw."""
    url = f"https://hn.algolia.com/api/v1/search?query={query}&tags=story"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = []
        for hit in data.get("hits", [])[:15]:
            results.append({
                "title": hit.get("title"),
                "url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "points": hit.get("points"),
                "comments": hit.get("num_comments"),
                "date": hit.get("created_at"),
            })
        return results
    except requests.RequestException as e:
        print(f"Error searching Hacker News: {e}")
        return []


def search_github_repos(query: str) -> list:
    """Search GitHub for repositories related to OpenClaw."""
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    headers = {"Accept": "application/vnd.github.v3+json"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = []
        for repo in data.get("items", [])[:15]:
            results.append({
                "name": repo.get("full_name"),
                "url": repo.get("html_url"),
                "description": repo.get("description"),
                "stars": repo.get("stargazers_count"),
                "forks": repo.get("forks_count"),
                "updated": repo.get("updated_at"),
            })
        return results
    except requests.RequestException as e:
        print(f"Error searching GitHub: {e}")
        return []


def search_devto(query: str) -> list:
    """Search DEV.to for articles about OpenClaw."""
    url = f"https://dev.to/api/articles?tag={query}&per_page=10"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = []
        for article in data:
            results.append({
                "title": article.get("title"),
                "url": article.get("url"),
                "reactions": article.get("public_reactions_count"),
                "comments": article.get("comments_count"),
                "date": article.get("published_at"),
                "author": article.get("user", {}).get("username"),
            })
        return results
    except requests.RequestException as e:
        print(f"Error searching DEV.to: {e}")
        return []


def update_hacker_news_file(results: list):
    """Update the Hacker News community file with new results."""
    filepath = os.path.join(OUTPUT_DIR, "community", "hacker-news", "hacker-news-latest.md")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        f.write("# Latest Hacker News Posts about OpenClaw\n\n")
        f.write(f"*Auto-updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*\n\n")
        f.write("| Title | Points | Comments | Date |\n")
        f.write("|-------|--------|----------|------|\n")
        
        for result in results:
            title = result['title'] or 'N/A'
            points = result['points'] or 0
            comments = result['comments'] or 0
            date = result['date'][:10] if result['date'] else 'N/A'
            f.write(f"| [{title}]({result['url']}) | {points} | {comments} | {date} |\n")
    
    print(f"Updated: {filepath}")


def update_github_file(results: list):
    """Update the GitHub tools file with new results."""
    filepath = os.path.join(OUTPUT_DIR, "tools", "github-repos-latest.md")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        f.write("# Latest GitHub Repositories for OpenClaw\n\n")
        f.write(f"*Auto-updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*\n\n")
        f.write("| Repository | Description | Stars | Forks |\n")
        f.write("|------------|-------------|-------|-------|\n")
        
        for result in results:
            name = result['name']
            desc = (result['description'] or 'N/A')[:60] + '...' if result['description'] and len(result['description']) > 60 else (result['description'] or 'N/A')
            stars = result['stars'] or 0
            forks = result['forks'] or 0
            f.write(f"| [{name}]({result['url']}) | {desc} | ⭐ {stars} | 🍴 {forks} |\n")
    
    print(f"Updated: {filepath}")


def update_devto_file(results: list):
    """Update the DEV.to blog file with new results."""
    filepath = os.path.join(OUTPUT_DIR, "community", "blogs", "devto-latest.md")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        f.write("# Latest DEV.to Articles about OpenClaw\n\n")
        f.write(f"*Auto-updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}*\n\n")
        f.write("| Title | Author | Reactions | Comments |\n")
        f.write("|-------|--------|-----------|----------|\n")
        
        for result in results:
            title = result['title'] or 'N/A'
            author = result['author'] or 'N/A'
            reactions = result['reactions'] or 0
            comments = result['comments'] or 0
            f.write(f"| [{title}]({result['url']}) | @{author} | ❤️ {reactions} | 💬 {comments} |\n")
    
    print(f"Updated: {filepath}")


def dedupe_results(results: list, key: str = "url") -> list:
    """Remove duplicate results by URL."""
    seen = set()
    unique = []
    for result in results:
        if result[key] not in seen:
            seen.add(result[key])
            unique.append(result)
    return unique


def main():
    """Main function to run all searches and update the repository."""
    print("=" * 50)
    print("OpenClaw Resource Repository Updater")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    all_hn_results = []
    all_github_results = []
    all_devto_results = []

    for term in SEARCH_TERMS:
        print(f"Searching for: {term}")

        # Hacker News
        hn_results = search_hacker_news(term)
        all_hn_results.extend(hn_results)
        print(f"  - Found {len(hn_results)} Hacker News posts")

        # GitHub
        github_results = search_github_repos(term)
        all_github_results.extend(github_results)
        print(f"  - Found {len(github_results)} GitHub repositories")

        # DEV.to
        devto_results = search_devto(term)
        all_devto_results.extend(devto_results)
        print(f"  - Found {len(devto_results)} DEV.to articles")

    # Dedupe and sort
    unique_hn = dedupe_results(all_hn_results)
    unique_hn.sort(key=lambda x: x.get("points") or 0, reverse=True)

    unique_github = dedupe_results(all_github_results)
    unique_github.sort(key=lambda x: x.get("stars") or 0, reverse=True)

    unique_devto = dedupe_results(all_devto_results)
    unique_devto.sort(key=lambda x: x.get("reactions") or 0, reverse=True)

    # Update files
    print()
    print("Updating repository files...")
    update_hacker_news_file(unique_hn)
    update_github_file(unique_github)
    update_devto_file(unique_devto)

    print()
    print("=" * 50)
    print("Update complete!")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)


if __name__ == "__main__":
    main()
