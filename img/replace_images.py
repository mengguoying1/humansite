# -*- coding: utf-8 -*-
import os
import re

# File list to scan
files = [
    "content/_index.md",
    "content/gameplay/_index.md",
    "content/gameplay/basic-controls.md",
    "content/gameplay/physics-tips.md",
    "content/guides/mansion.md",
    "content/guides/factory.md",
    "content/multiplayer/_index.md",
    "content/about/_index.md",
    "content/media/_index.md"
]

# Patterns and their local replacements
replacements = [
    (r"https?://[^\s\"')]+255ce652883cdb8fc0dc4dac6697db71aa535f3f[^\s\"')]+", "/img/mansion.jpg"),
    (r"https?://[^\s\"')]+94f4e124f87b033d985f3ff542ac8d2d7195d106[^\s\"')]+", "/img/climbing.jpg"),
    (r"https?://[^\s\"')]+eca0a2596d4b9e746154ee95571eb19db622e25e[^\s\"')]+", "/img/factory.jpg"),
    (r"https?://[^\s\"')]+88cfb9c5b0e71d00d17310326c50c55bb4c0a77c[^\s\"')]+", "/img/swinging.jpg"),
    (r"https?://[^\s\"')]+045dbf6a11c00886d9b1fee5bd818686680463f9[^\s\"')]+", "/img/multiplayer.jpg"),
    (r"https?://upload\.wikimedia\.org/wikipedia/en/e/e5/Human_Fall_Flat_cover_art\.jpg", "/img/cover.jpg")
]

for filename in files:
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    print(f"Processing {filename}...")
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Specifically for content/_index.md, use hero_banner.jpg for the first image
    original_content = content
    
    for pattern, local_path in replacements:
        if filename == "content/_index.md" and "255ce652883cdb8fc0dc4dac6697db71aa535f3f" in pattern:
            # Replace with hero_banner.jpg on homepage
            content = re.sub(pattern, "/img/hero_banner.jpg", content)
        else:
            content = re.sub(pattern, local_path, content)
            
    if content != original_content:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename} with local image paths.")
    else:
        print(f"No changes in {filename}.")

print("Image path replacement complete!")
