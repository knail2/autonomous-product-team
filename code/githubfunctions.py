from github import Auth, Github

# AutoGen function calling - A more reliable Solution
# https://www.youtube.com/watch?v=dCBXFjjOD5c
# we need functions to authenticate
# download a file to share with the coder

# then we need a function to send pull request

def get_auth_token():
    with open('gh_auth_token', 'r') as file:
        # Read the contents of the file into a variable
        auth_token = file.read()
    return auth_token

def get_spiderman_code():
    auth = Auth.Token(get_auth_token())
    g = Github(auth=auth)
    repo = g.get_repo("knail2/development-project")
    file = repo.get_contents("code/spiderman.py")
    file_content = file.decoded_content.decode("utf-8")
    return file_content

def send_pull_request(new_content, branch_name, commit_description):
    #with open(updated_file_name, 'r') as file:
    #    new_content = file.read()
    auth = Auth.Token(get_auth_token())
    g = Github(auth=auth)
    repo = g.get_repo("knail2/development-project")
    source = repo.get_branch("main")
    new_branch = "refs/heads/" + branch_name
    repo.create_git_ref(ref=new_branch, sha=source.commit.sha)
    contents = repo.get_contents("code/spiderman.py", ref=new_branch)
    repo.update_file(contents.path, 
                     commit_description, 
                     new_content, 
                     contents.sha, 
                     branch=new_branch)
    pr = repo.create_pull(title="pull request for " + commit_description, 
                          body="Description of the PR for" + commit_description, 
                          head=new_branch, base="main")
    

    