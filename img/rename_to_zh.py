# -*- coding: utf-8 -*-
import os

def rename_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md") and not filename.endswith(".zh-cn.md"):
                old_path = os.path.join(dirpath, filename)
                new_filename = filename[:-3] + ".zh-cn.md"
                new_path = os.path.join(dirpath, new_filename)
                print(f"Renaming {old_path} -> {new_path}")
                
                # Check if target already exists. If yes, delete it first to prevent rename error.
                if os.path.exists(new_path):
                    os.remove(new_path)
                os.rename(old_path, new_path)

if __name__ == "__main__":
    rename_files("content")
    print("All Chinese files renamed successfully!")
