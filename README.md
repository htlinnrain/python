ssh-keygen -t ed25519 -C "htlinnrain@gmail.com"

Configure ~/.ssh/config with host aliases for each account:

text
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_account1

Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_account2

    Use git@github-personal:username/repo.git and git@github-work:username/repo.git for remotes.
