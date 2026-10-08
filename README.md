# GDIP

Click here for [How to use Git](#How-to-use-Git)
## Project format
- [source](source) contains the actual robot code and 
- [cad](cad) contains robot model cad and hardware diagrams
- [writeup](writeup) contains MD files of our writeup. will be converted to docx / pdf upon finishing
- [documentation](documentation) contains md files documenting the design of the robot. may not be needed or used

## Source
[source](source)
- main py file
- ?

## CAD
[cad](cad)
- testtube.cad
- testtubehuman.cad
- gripper.cad
- newarm.cad

## Writeup
[writeup](writeup)
- ?

## Documentation
[documentation](documentation)
- ?




## How to use Git
setup written with commands, you may just use a visual(vscode/gitdesktop) one in that case assume the buttons from the command names
### Setup
- go to destination (/Documents)
- git clone git@github.com:CharlieJP05/GDIP.git
- git is created at (Documents/GDIP)
### Editing
- Do whatever editing you want to do
- git commit -m "Added function to move wrist" `<- Saves current additions as a commit`
- git push `<- Pushes all commits to remote (github)`
### Branching
- you can do editing on a seperate branch to keep changes seperated for the moment and bring them back to the MAIN branch later when they are more finished in order to not break the code or allow multiple people to work at once
- create branch main -> AI_Integration
- do edits on branch
- when features complete, merge AI_Integration branch back to main
