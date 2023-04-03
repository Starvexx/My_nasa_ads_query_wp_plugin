# My_nasa_ads_query_wp_plugin
A Wordpress plugin to query the SAO/NASA ADS (Smithsonian Astrophysical Observatory for the National Aeronatics and Space Administration Astrophysics Data Service) https://ui.adsabs.harvard.edu/

This Wordpress plugin allows you to get publications from the SAO/NASA ADS, and display them on you homepage. At the moment this plugin only allows you to get publications gathered in an ADS library by placing your ADS API token and the ADS library ID into the respective variables in the `query.py` script located inside the `wp_ads_plugin` folder. 

In order for this plugin to work, you will need an API token and a public ADS library containing all publications you want to display on your webpage.

## Installation

If you wish to install this plugin, you need to first download this repository to your computer and modify the `query.py` file inside the `wp_ads_plugins` folder.

### Preparation
Edit lines 8 and 11, and replace the `token` placeholder and `library_id` placeholder with your own API token (get yours here: https://ui.adsabs.harvard.edu/help/api/) and the library ID of your library at the ADS. You can get the library ID from the public URL your library. For instance, when logged in to your ADS account, go to ADS Libraries, select the library you want to query, and go to "Manage Access". The public address is shown in a notification box. The library ID are string of characters after the last `/`, and the whole URL should look something like this:

    https://ui.adsabs.harvard.edu/public-libraries/<your_library_id>

### Packing and upload
Once you have edited the two lines as described above, you can go ahead and compress the `wp_ads_plugin` into a zip file. This zip file can then be imported to your webpage by using the wordpress plugin manager, by clicking on "Add New", and then by clicking on "Upload Plugin". Select the `wp_nasa_plugin.zip` file you have just created, and activate the plugin after the upload has finished.

## Use the plugin on your webpage

This plugin uses shortcode to display the publication entries from your ADS library on your webpage. So to do so, you add a new block to the page on which you want to show your publications. Select the shortcode block (often represented by a symbol showing square brackets around a forward slash `[/]`) and add the following line to it.

    [nasa_ads_library]
