from argparse import ArgumentParser
import subprocess
import os
import shutil

def take_paths():
    parser = ArgumentParser(description="Download folder from GitHub")
    parser.add_argument('url', help='URL to download', type=str)
    parser.add_argument('path',  help='Path to download', type=str)
    parser.add_argument('folder', help='Folder wanted to download in repo', type=str)
    parser.add_argument('--branch', help='Branch to download', type=str, default='main')
    return parser.parse_args()

def mk_mv_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_folder(url, branch, folder, path):
    repo_name = url.split('/')[-1].replace('.git', '')
    if os.path.exists(repo_name):
        print(f"Directory '{repo_name}' already exists. Removing it...")
        shutil.rmtree(repo_name)
    try:
        subprocess.run(['git', 'clone', '--no-checkout',url], check=True)
        os.chdir(repo_name)
        subprocess.run(['git', 'sparse-checkout', 'init', '--cone'], check=True)
        subprocess.run(['git', 'sparse-checkout', 'set', folder], check=True)
        subprocess.run(['git', 'checkout', branch], check=True)

        target_path = os.path.abspath(path)
        os.chdir('..')
        shutil.move(repo_name, target_path)

        print(f"Folder '{folder}' has been downloaded to '{target_path}'.")

    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        os.chdir('..') 
        if os.path.exists(repo_name):
            shutil.rmtree(repo_name)

if __name__ == '__main__':
    args = take_paths()
    mk_mv_dir(args.path)
    download_folder(args.url, args.branch, args.folder, args.path)