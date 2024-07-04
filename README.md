# Ichido AI And LLM Bot Blocker

<p align="center">
  <img src="docs/art.png" />
</p>

The AI/LLM bot blocker web server, firewall, and robots.txt config generator used in production by the [Ichido Search Engine](https://ichi.do/). These configs block known large AI and LLM bots from accessing your site content, while still allowing classical search engines and legitimate users to access content. Supports the following web servers, firewalls, and standards:

<p align="center">
  <img src="docs/combined.png" />
</p>

| Server/Firewall | Blocked      |
| --------------- | ------------ |
| Iptables        | IP Addresses |
| Apache          | User-Agent   |
| Nginx           | User-Agent   |
| Lighttpd        | User-Agent   |
| Caddy           | User-Agent   |
| IIS             | User-Agent   |
| Robots.txt      | User-Agent   |

In total there are 16 variants of config files, of which you'll only need 2 with the **recommended** config (1 web server config and 1 robots.txt), or 3 with the **non-recommended** config (1 web server config, 1 robots.txt, and 1 firewall config):

* The **recommended** config will block most AI bots with a low false positive rate, while still allowing archival services and classical search engines access to site content.
* The **non-recommended** will config aggressively blocks bots and site scrapers (including AI bots, classical search engines, and archival services), but **will likely have many false positives**. It is recommended for nearly all use cases to use the **recommended** config.

The config files can be built manually from source, or prebuilt files can be downloaded from [Ichido's file server](https://files.ichi.do/). Recommended config prebuilt files are prefixed with `recommended-` and non-recommended files with `non-recommende-`. Below are instructions for applying the configurations.

# Usage

## Step 1. Download An AI Bot Blocker Robots.txt.

1. Download the robots.txt file and add it to the root of your web content (should be reachable at `https://\<your_site\>/robots.txt`).

```bash
wget https://files.ichi.do/recommended-robots-block-ai-bots.conf /var/www/html/<web_root>/robots.txt
```

## Step 2. Download An AI Bot Blocker Web Server Config.

### Apache

<p align="center">
  <img src="docs/apache.png" />
</p>

For shared hosting, use the `.htaccess` file instructions below.

1. Enable the rewrite module.

```bash
sudo a2enmod rewrite
```

2. Download the config file into apache's `conf-available` directory:

```bash
sudo wget https://files.ichi.do/recommended-apache-block-ai-bots.conf -O /etc/apache2/conf-available/block-ai-bots.conf
```

3. Create a symbolic link to the config in `/etc/apache2/conf-enabled/`

```bash
ln -s /etc/apache2/conf-available/block-ai-bots.conf /etc/apache2/conf-enabled/
```

4. Restart apache.

```bash
sudo service apache2 restart
```

#### .htaccess

1. Download the config file.

```bash
sudo wget https://files.ichi.do/recommended-htaccess-block-ai-bots.conf
```

2. Merge the config with your existing `.htaccess` file, either manually using your hosting provider tools or with this command.

```bash
cat .htaccess recommended-htaccess-block-ai-bots.conf > temp.conf
mv temp.conf .htaccess
```

### Nginx

<p align="center">
  <img src="docs/nginx.png" />
</p>

1. Download the config file into nginx's `modules-available` directory:

```bash
sudo wget https://files.ichi.do/recommended-nginx-block-ai-bots.conf -O /etc/nginx/modules-available/11-block-ai-bots.conf
```

2. Include the config in your `server` blocks after the `listen` directives:

```nginx
# Ichido AI Bot Blocker.
include /etc/nginx/modules-available/11-block-ai-bots.conf;
```

3. Restart nginx.

```bash
sudo service nginx restart
```

### Lighttpd

<p align="center">
  <img src="docs/lighttpd.png" />
</p>

1. Download the config file into lighttpd's `conf-available` directory:

```bash
sudo wget https://files.ichi.do/recommended-lighttpd-block-ai-bots.conf -O /etc/lighttpd/conf-available/11-block-ai-bots.conf
```

2. Create a symbolic link to the config in `/etc/lighttpd/conf-enabled/`

```bash
sudo ln -s /etc/lighttpd/conf-available/11-block-ai-bots.conf /etc/lighttpd/conf-enabled/
```

3. Restart lighttpd.

```bash
sudo service lighttpd restart
```

### Caddy

<p align="center">
  <img src="docs/caddy.png" />
</p>

1. Make directories to store caddy config files.

```bash
sudo mkdir -p /etc/caddy/conf-available/
sudo mkdir -p /etc/caddy/conf-enabled/
```

2. Download the config file into `/etc/caddy/conf-available/`:

```bash
sudo wget https://files.ichi.do/recommended-caddy-block-ai-bots.conf -O /etc/caddy/conf-available/11-block-ai-bots.conf
```

3. Create a symbolic link to the config in `/etc/caddy/conf-enabled/`

```bash
sudo ln -s /etc/caddy/conf-available/11-block-ai-bots.conf /etc/caddy/conf-enabled/
```

4. Import the config file in your site blocks. For example:

```caddy
# Ichido AI Bot Blocker.
:80 {
    import /etc/caddy/conf-enabled/11-block-ai-bots.conf
}
```

5. Restart caddy.

```bash
sudo service caddy restart
```

### IIS

<p align="center">
  <img src="docs/iis.png" />
</p>

TODO

## (Optional) Step 3. Download An AI Bot Blocker Firewall Config.

### Iptables

1. Install `iptables-persistent`.

```bash
sudo apt-get install -y iptables-persistent
```

2. Download the config file into `/etc/iptables/rules.v4`:

```bash
sudo wget https://files.ichi.do/non-recommended-iptables-block-ai-bots.conf -O /etc/iptables/rules.v4
```

3. Restart iptables.

```bash
sudo service iptables restart
```

## Contributing

For ease of contribution, this repo is hosted on Github and mirrored on [Ichido's Software Forge](https://git.ichi.do/anthony/ai-bot-blocker/). If you have a Github account, you can contribute using Github's standard workflow, but if you do not have a Github account you can still contribute via email patches using the workflow below:

1. Clone this repo:

```bash
git clone https://git.ichi.do/anthony/ai-bot-blocker
cd ai-bot-blocker
```

2. Add your name and an email address to the locally cloned repo:

```bash
git config user.name "<name>"
git config user.email "<email>"
```

3. Make changes to the source code.
4. Add those changes and commit:

```bash
git add .
git commit -m "ADD: new commit."
```

5. Create a patch file from the new commit:

```bash
# Use HEAD~1 for 1 commit, HEAD~2 for 2 commits, etc.
git diff HEAD~1 > diff.patch
```

6. Send the patch file to \<<anthony.m.mancini@protonmail.com>\> through email.

## License

(C) Anthony Mancini 2024. Licensed under the AGPL-3.0 (see [LICENSE.txt](LICENSE.txt)).

## Contact

* Anthony Mancini \<<anthony.m.mancini@protonmail.com>\>
