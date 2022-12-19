# Introduction
This activity was made using and venv

# Instructions
> Note: Don't forget to do not include the text inside these: < > (including also these characters and spaces)

1. Run this command to create
```shell
py -m venv selenium <or-the-name-that-you-want>
```

2. To activate the venv
```shell
.\selenium <or-the-name-that-you-chose> \Scripts\activate
```
> If you want to close the environment run:
```shell
deactivate
```
3. Then to install the dependencies from the requirements.txt file
```shell
pip install -r requirements.txt
```

---
## Extra information
1. If you add more dependencies/libraries, you will have to update the requirements.txt file, to do this use the next command

```shell
pip freeze > requirements.txt

```

2. This script needs a .env file with the next structure
```env
WEBDRIVER_PATH = "./path/to/the/webdriver"
```

3. The script accepts only Chrome or Edge webdriver, so it can only used with these two