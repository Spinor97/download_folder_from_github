# Download Folder from GitHub

This is a simple project that helps download a folder from a repository on GitHub by running a command.

## Usage

To use this project, run the following command:

```sh
# Replace <repo-url> with the URL of the GitHub repository
#Repleace <download path> with the path you want to download in
# Replace <folder-path> with the path to the folder you want to download
# Branch name is optional
pyhton python download_folder_from_github.py <repo-url> <download path> <folder-path> --branch <branch name>
```

## Known Issues

- Sometimes the downloaded files in the folder cannot be correctly deleted due to access problem of some files in the folder.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.