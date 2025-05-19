

# fohshgir

**Fohshgir** is a Telegram bot that automatically **mutes users who use offensive language** in groups. Designed for group admins who want peace of mind and a clean environment, this bot handles moderation so you don't have to.

## ⚙️ Prerequisites

Make sure the following requirements are met before installation:

* **Operating System**: Ubuntu
* **Permissions**: Root or sudo access

## 🚀 Installation

To install the `fohshgir` bot, run the following commands:

1. **Download and prepare the installer**:

   ```bash
   sudo bash -c "$(curl -sL https://raw.githubusercontent.com/erfjab/fohshgir/master/install.sh)" @ install-script
   ```

2. **Install the bot**:

   ```bash
   fohshgir install
   ```

3. **Register as a system service**:

   ```bash
   fohshgir install-service
   ```

4. **Start the bot**:

   ```bash
   fohshgir start
   ```

---

### 📦 What This Installation Does

* ✅ Installs all necessary dependencies
* 🧬 Clones the official `fohshgir` GitHub repository
* 🐍 Sets up an isolated Python environment
* 🔧 Registers the bot as a background service
* ▶️ Starts the bot and keeps it running

---

## 🧑‍💻 Usage

After installation, manage the bot with:

```bash
fohshgir <command>
```

### Available Commands

| Command     | Description                                      |
| ----------- | ------------------------------------------------ |
| `install`   | Installs the bot and its dependencies            |
| `start`     | Starts the bot service                           |
| `stop`      | Stops the bot service                            |
| `restart`   | Restarts the bot service                         |
| `status`    | Shows the current status of the service          |
| `logs`      | Displays the bot's live logs                     |
| `update`    | Pulls latest changes and applies updates         |
| `uninstall` | Removes the bot and all related files completely |
| `help`      | Lists all available commands                     |

---

## 📁 Directory Structure

* **Installation Path**: `/opt/erfjab/fohshgir`
* **Log File**: `/opt/erfjab/fohshgir/fohshgir.log`
* **Systemd Service**: `/etc/systemd/system/fohshgir.service`

---

## ❌ Uninstallation

To completely remove `fohshgir`, run:

```bash
sudo fohshgir uninstall
```
 

