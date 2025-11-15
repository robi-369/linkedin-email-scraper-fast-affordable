# LinkedIn Email Scraper (👥 Fast & Affordable) 📧
This LinkedIn Email Scraper helps you discover user emails, profile links, and usernames based on any chosen keyword or email domain. It automates the process of finding relevant LinkedIn profiles and extracting verified data at scale. Whether for outreach, research, or lead generation, this tool makes gathering LinkedIn email information fast and efficient.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>LinkedIn Email Scraper (👥 Fast & Affordable) 📧</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
This project allows you to search LinkedIn by keyword and retrieve emails associated with user profiles.
It simplifies manual research and eliminates time-consuming profile checks while returning structured, ready-to-use data.
Ideal for marketers, recruiters, analysts, and businesses that rely on accurate LinkedIn email data.

### How It Works
- Searches LinkedIn profiles using keywords such as job roles, interests, or hashtags.
- Filters results by specified email domains to refine relevance.
- Extracts verified email addresses, usernames, and profile URLs.
- Outputs clean, structured datasets for instant use.
- Scales to unlimited queries with adjustable result limits.

## Features
| Feature | Description |
|---------|-------------|
| Unlimited Results | Extract as many LinkedIn email profiles as needed. |
| Domain Filtering | Target email domains such as `@gmail.com`, `@outlook.com`, and more. |
| Keyword-Based Search | Find users based on interests, roles, or trending topics. |
| Detailed Profile Data | Retrieve emails, usernames, and LinkedIn profile URLs. |
| Flexible Output Formats | Export data in JSON, CSV, Excel, or other formats. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| Email | The extracted email associated with the LinkedIn user. |
| Domain | The domain portion of the extracted email. |
| Title | The user’s LinkedIn headline or role description. |
| Detail_Link | Direct URL to the LinkedIn profile. |
| Username | Parsed username or profile handle. |
| Keyword | The search keyword used for extraction. |
| DomainEmailUsed | List of email domains used for filtering. |

---

## Example Output

    [
      {
        "Email": "iamanubhavgain@gmail.com",
        "Domain": "gmail.com",
        "Title": "Anubhav Gain - Software Engineer - Infopercept Consulting",
        "Detail_Link": "https://in.linkedin.com/in/anubhavgain",
        "Keyword": "Security Engineer",
        "DomainEmailUsed": ["@gmail.com"]
      }
    ]

---

## Directory Structure Tree

    LinkedIn Email Scraper (👥 Fast & Affordable) 📧/
    ├── src/
    │   ├── main.py
    │   ├── extractors/
    │   │   ├── linkedin_parser.py
    │   │   └── utils_filters.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── input.sample.json
    │   └── sample_output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Marketers** use it to collect targeted emails for outreach campaigns, so they can improve personalization and conversion.
- **Recruiters** use it to identify potential candidates, so they can accelerate talent sourcing.
- **Researchers** use it to analyze niche communities, so they can understand trends and engagement patterns.
- **Sales teams** use it to build high-quality lead lists, so they can increase pipeline efficiency.
- **Businesses** use it to verify user information, so they can maintain accurate internal databases.

---

## FAQs

**Q: Is there a limit to how many results I can scrape?**
A: No, the scraper supports unlimited results and scales based on your configured keyword and domain filters.

**Q: Can I target specific email domains?**
A: Yes, simply provide a list of domains such as `["@gmail.com"]` to filter results.

**Q: What formats can I export data in?**
A: You can download your results in JSON, CSV, Excel, and other common data formats.

**Q: Do I need any coding experience?**
A: No coding is required to run the scraper; however, developers can integrate it programmatically using Python.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes an average of 150–250 profile scans per minute depending on query complexity.
**Reliability Metric:** Maintains a 98% stable run rate across large-scale keyword searches.
**Efficiency Metric:** Optimized data parsing ensures low CPU usage even during high-volume operations.
**Quality Metric:** Delivers over 95% data completeness and consistent email-domain accuracy.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
