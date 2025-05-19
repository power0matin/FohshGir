[English](/README.md) | [فارسی](/README.fa_IR.md)

# fohshgir

**Fohshgir** is a Telegram bot that automatically **mutes users who use offensive language** in groups. Designed for group admins who want a peaceful and clean environment, this bot handles moderation so you don’t have to worry about managing inappropriate messages.

---

## ⚙️ Prerequisites

Before installing and running the bot, please ensure:

* Operating System: **Ubuntu**
* Permissions: **Root or sudo access**

---

## 🚀 Installation Guide

To install the `fohshgir` bot, follow these steps:

1. **Download and prepare the installation script:**

```bash
sudo bash -c "$(curl -sL https://raw.githubusercontent.com/erfjab/fohshgir/master/install.sh)" @ install-script
```

2. **Install the bot:**

```bash
fohshgir install
```

3. **Register the bot as a system service:**

```bash
fohshgir install-service
```

4. **Start the bot:**

```bash
fohshgir start
```

---

### 📦 What This Installation Does

* Installs all necessary dependencies
* Clones the official `fohshgir` repository from GitHub
* Sets up an isolated Python environment
* Registers the bot as a background system service (systemd)
* Starts the bot and keeps it running continuously

---

## 🧑‍💻 Usage and Management

After installation, you can manage the bot using:

```bash
fohshgir <command>
```

### Available Commands

| Command     | Description                                  |
| ----------- | -------------------------------------------- |
| `install`   | Installs the bot and its dependencies        |
| `start`     | Starts the bot service                       |
| `stop`      | Stops the bot service                        |
| `restart`   | Restarts the bot service                     |
| `status`    | Shows the current status of the service      |
| `logs`      | Displays live logs of the bot                |
| `update`    | Pulls the latest changes and updates the bot |
| `uninstall` | Completely removes the bot and related files |
| `help`      | Lists all available commands                 |

---

## 📁 Directory Structure

* Installation path: `/opt/erfjab/fohshgir`
* Log file: `/opt/erfjab/fohshgir/fohshgir.log`
* Systemd service file: `/etc/systemd/system/fohshgir.service`

---

## ❌ Uninstallation

To completely remove `fohshgir` and clean up all related files, run:

```bash
sudo fohshgir uninstall
```

---

## 📞 Support and Contact

If you encounter any issues or have questions, feel free to open an issue on the GitHub repository or contact the developer.
