## Install GIT on macOS
There are several ways to install Git on a Mac. In fact, if you've installed XCode (or it's Command Line Tools), Git may already be installed. To find out, open a terminal and enter

```bash
$ git --version
```
Apple actually maintain and ship their own [fork of Git](https://opensource.apple.com/source/Git/), but it tends to lag behind mainstream Git by several major versions. You may want to install a newer version of Git using the methods below:

### Git for Mac Installer
The easiest way to install Git on a Mac is via the stand-alone installer:

1. Download the latest [Git for Mac installer](https://sourceforge.net/projects/git-osx-installer/files/).

2. Follow the prompts to install Git.

3. Open a terminal and verify the installation was successful by typing
```bash
$ git --version
```
```bash
git version 2.9.2
```
4. Configure your Git username and email using the following commands, replacing Jin's name with your own. These details will be associated with any commits that you create:
```bash
$ git config --global user.name "Jin Zhou"
```
```bash
$ git config --global user.email "jin_zhou@unigroup.com"
```
5. Check the configurations.
```bash
$ git config --list
```
## Install GIT on Windows
1. Download the latest Git for [Windows installer](https://gitforwindows.org/).

2. When you've successfully started the installer, you should see the Git Setup wizard screen. Follow the Next and Finish prompts to complete the installation. The default options are pretty sensible for most users.

3. Open a Command Prompt (or Git Bash if during installation you elected not to use Git from the Windows Command Prompt).

4. Run the following commands to configure your Git username and email using the following commands, replacing Jin's name with your own. These details will be associated with any commits that you create:
```bash
$ git config --global user.name "Jin Zhou"
```
```bash
$ git config --global user.email "jin_zhou@unigroup.com"
```
5. Need to config core.autocrlf to be true if it is not set by default to avoid the line change issue for Windows users.
```bash
$ git config --local core.autocrlf true
```
6. Check the configurations.
```bash
$ git config --list
```
## Access GitLab with SSH keys
### Generate an SSH key pair
If you do not have an existing SSH key pair, generate a new one:
1. Open a terminal.
2. Run [ssh-keygen](https://en.wikipedia.org/wiki/Ssh-keygen) -t followed by the key type and an optional comment. This comment is included in the .pub file that’s created. You may want to use an email address for the comment.

For example, for 2048-bit RSA:
```bash
ssh-keygen -t rsa -b 2048 -C "<comment>"
```
3. Press Enter. Output similar to the following is displayed:
```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
```
4. Accept the suggested filename and directory, unless you are generating a deploy key or want to save in a specific directory where you store other keys.

   You can also dedicate the SSH key pair to a specific host.

5. Specify a passphrase:
```bash
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```
A confirmation is displayed, including information about where your files are stored.
###Add an SSH key to your GitLab account
To use SSH with GitLab, copy your public key to your GitLab account:

1. Copy the contents of your public key file. You can do this manually or use a script. For example, to copy an ED25519 key to the clipboard:

#### macOS
```bash
tr -d '\n' < ~/.ssh/id_rsa.pub | pbcopy
```
#### Git Bash on Windows
```bash
cat ~/.ssh/id_rsa.pub | clip
```
Replace id_ed25519.pub with your filename. For example, use id_rsa.pub for RSA.

2. Sign in to GitLab.
3. On the top bar, in the upper-right corner, select your avatar.
4. Select **Preferences**.
5. On the left sidebar, select **SSH Keys**.
6. In the Key box, paste the contents of your public key. If you manually copied the key, make sure you copy the entire key, which starts with ssh-rsa, ssh-dss, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, ecdsa-sha2-nistp521, ssh-ed25519, sk-ecdsa-sha2-nistp256@openssh.com, or sk-ssh-ed25519@openssh.com, and may end with a comment.
7. In the Title box, type a description, like Work Laptop or Home Workstation.
8. Optional. Select the Usage type of the key. It can be used either for Authentication or Signing or both. Authentication & Signing is the default value.
9. Optional. Modify the default expiration date. In:

   - GitLab 13.12 and earlier, the expiration date is informational only. It doesn’t prevent you from using the key. Administrators can view expiration dates and use them for guidance when deleting keys.

   - GitLab checks all SSH keys at 02:00 AM UTC every day. It emails an expiration notice for all SSH keys that expire on the current date. (Introduced in GitLab 13.11.)

   - GitLab checks all SSH keys at 01:00 AM UTC every day. It emails an expiration notice for all SSH keys that are scheduled to expire seven days from now. (Introduced in GitLab 13.11.)
10. Select Add key.

#### Verify that you can connect
Verify that your SSH key was added correctly.

The following commands use the example hostname gitlab.example.com. Replace this example hostname with your GitLab instance’s hostname, for example, git@gitee.unigroupinc.com.
1. Open a terminal and run this command, replacing gitlab.example.com with your GitLab instance URL:
```bash
ssh -T git@gitee.unigroupinc.com
```
If this is the first time you connect, you should verify the authenticity of the GitLab host. If you see a message like:
```bash
The authenticity of host 'gitlab.example.com (35.231.145.151)' can't be established.
ECDSA key fingerprint is SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'gitlab.example.com' (ECDSA) to the list of known hosts.
```
Type yes and press Enter.

Run the
```bash
ssh -T git@gitlab.example.com
```
command again. You should receive a
```bash
Welcome to GitLab, @username!
```
message.
If the welcome message doesn’t appear, you can troubleshoot by running ssh in verbose mode:
```bash
ssh -Tvvv git@gitlab.example.com
```

