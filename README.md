### **Project Overview: Export Data from MyFitnessPal to Grafana** 📊📱

The requirements:  
MyFitnessPal is a mobile app used to track food & energy intake, exercise, and more. It supports CSV data export (e.g., through email) to facilitate archival, but this style is a bit antiquated for manual viewing.

A simple website that accepts CSV exports and renders nice visual representations using Grafana would be much better for users. This should be feasible to complete in a few days since all of the major components already exist.

### **These are the results of the project**

![Screenshot 2025-03-18 183008](https://github.com/user-attachments/assets/25768d72-3546-477b-97de-7242bf218dee)  
![Screenshot 2025-03-18 182853](https://github.com/user-attachments/assets/e56c35b3-6653-455a-b125-1a93d622ecc6)  
![Screenshot 2025-03-18 182910](https://github.com/user-attachments/assets/e1690f2f-1c62-48eb-b44b-e4430ec2d6b0)  
![Screenshot 2025-03-18 182922](https://github.com/user-attachments/assets/e0b6cbf0-8a36-408d-8af7-1430252b5f4b)  
![Screenshot 2025-03-18 182947](https://github.com/user-attachments/assets/4cf08ce7-7c81-4893-aa96-bd13667bfece)

### **What I Did** 💻🔧

Created a `nutrition.csv` file with data fields like **Date**, **Calories**, **Protein (g)**, **Carbs (g)**, and **Fat**.

Moved the file to `/var/lib/grafana/csv/` and set appropriate permissions:

```bash
sudo chown grafana:grafana /var/lib/grafana/csv/nutrition.csv
sudo chmod 644 /var/lib/grafana/csv/nutrition.csv
```

Installed Grafana on your Linux server and accessed it via `http://<server-ip>:3000`.

Installed the `marcusolsson-csv-datasource` plugin to enable CSV support:

```bash
sudo grafana-cli plugins install marcusolsson-csv-datasource
sudo systemctl restart grafana-server
```

Added the CSV file as a data source in Grafana, specifying its path (`/var/lib/grafana/csv/nutrition.csv`).  
Configured delimiter settings (comma-separated) and ensured headers were recognized.

Created a new dashboard and added a panel.

Verified that the data was loaded into Grafana by displaying it in **Table View**.

Resolved the error **"Data is missing a number field"** by mapping fields correctly:  
- Set **Date** as the **Time Field** ⏰.  
- Set **Calories**, **Protein (g)**, **Carbs (g)**, and **Fat** as numeric fields 🔢.

And successfully visualized data! 🎉📊

