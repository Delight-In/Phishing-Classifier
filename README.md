# Phishing Website Detection Model

### Dataset Description

The dataset contains information about websites and is used to predict whether a website is phishing or legitimate. The dataset has the following columns:

| Column Name                        | Description                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| **having_IP_Address**               | Indicates if the website uses an IP address (1 for yes, 0 for no).                                |
| **URL_Length**                      | Length of the URL.                                                                                 |
| **Shortining_Service**              | Indicates whether the URL is shortened by a service like Bit.ly (1 for yes, 0 for no).             |
| **having_At_Symbol**                | Indicates if the URL contains the "@" symbol (1 for yes, 0 for no).                               |
| **double_slash_redirecting**        | Indicates if the URL contains "double slashes" (1 for yes, 0 for no).                             |
| **Prefix_Suffix**                   | Indicates whether the URL has a prefix or suffix (1 for yes, 0 for no).                           |
| **having_Sub_Domain**               | Indicates if the URL has a sub-domain (1 for yes, 0 for no).                                      |
| **SSLfinal_State**                  | The final SSL state of the website (1 for valid SSL, 0 for invalid SSL).                          |
| **Domain_registeration_length**     | Length of the domain registration in years.                                                       |
| **Favicon**                          | Indicates whether the website has a favicon (1 for yes, 0 for no).                                |
| **port**                             | Port number used by the website.                                                                   |
| **HTTPS_token**                     | Indicates if the URL contains "HTTPS" (1 for yes, 0 for no).                                      |
| **Request_URL**                     | Indicates if the URL contains a "request" (1 for yes, 0 for no).                                 |
| **URL_of_Anchor**                   | Indicates if the anchor text of the URL contains the URL itself (1 for yes, 0 for no).             |
| **Links_in_tags**                   | Indicates whether the page contains "links" in HTML tags (1 for yes, 0 for no).                   |
| **SFH**                             | Indicates if the page uses a "Server Form Handler" (1 for yes, 0 for no).                         |
| **Submitting_to_email**              | Indicates if the form is submitting to an email (1 for yes, 0 for no).                             |
| **Abnormal_URL**                    | Indicates if the URL is considered abnormal (1 for yes, 0 for no).                                |
| **Redirect**                         | Indicates if the URL redirects to another page (1 for yes, 0 for no).                             |
| **on_mouseover**                    | Indicates if the page uses the "mouseover" event (1 for yes, 0 for no).                            |
| **RightClick**                       | Indicates if the website disables right-click functionality (1 for yes, 0 for no).                |
| **popUpWidnow**                      | Indicates if the website contains a popup window (1 for yes, 0 for no).                           |
| **Iframe**                           | Indicates if the website contains an iframe (1 for yes, 0 for no).                                |
| **age_of_domain**                   | Age of the domain in years.                                                                       |
| **DNSRecord**                        | Indicates if the website has a valid DNS record (1 for yes, 0 for no).                             |
| **web_traffic**                      | The amount of web traffic the website receives.                                                   |
| **Page_Rank**                        | The page rank of the website.                                                                      |
| **Google_Index**                     | Indicates if the website is indexed by Google (1 for yes, 0 for no).                              |
| **Links_pointing_to_page**           | The number of links pointing to the website.                                                      |
| **Statistical_report**               | Indicates whether a statistical report is present for the website (1 for yes, 0 for no).         |
| **Result**                           | The target label: 1 indicates phishing, 0 indicates legitimate.                                     |
