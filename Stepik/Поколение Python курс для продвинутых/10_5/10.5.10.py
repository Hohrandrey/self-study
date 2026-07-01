folder_system = {
    'Root': ['FolderA', 'FolderB', 'FolderC'],
    'FolderA': ['Subfolder1', 'Subfolder2'],
    'FolderB': ['Subfolder3', 'Subfolder4'],
    'FolderC': ['Subfolder5', 'Subfolder6'],
    'Subfolder1': ['Document1', 'Document2'],
    'Subfolder2': ['Document3', 'Document4'],
    'Subfolder3': ['Document5', 'Document6'],
    'Subfolder4': ['Document7', 'Document8'],
    'Subfolder5': ['Document9', 'Document10'],
    'Subfolder6': ['Document11', 'Document12'],
}

def is_subfolder(folder_dict, subfolder, folder):
    if folder not in folder_dict:
        return False
    if subfolder in folder_dict[folder]:
        return True
    for elem in folder_dict[folder]:
        if is_subfolder(folder_dict, subfolder, elem):
            return True
    return False


print(is_subfolder({}, 'folder1', 'folder2'))