#!/usr/pkg/bin/python3.13

#
# Time-stamp: <2025/05/05 18:28:44 (UT+08:00) daisuke>
#

# importing git module
import git

# URL of repository
url_repo = 'https://github.com/astrocatalogs/sne-2015-2019.git'

# directory name of downloaded repository
dir_repo = 'osc_2015_2019'

# downloading repository
repo = git.Repo.clone_from (url_repo, dir_repo)
