Create a system user for Prometheus:

 sudo useradd --no-create-home --shell /bin/false prometheus
Create the directories in which we'll be storing our configuration files and libraries:

 sudo mkdir /etc/prometheus
 sudo mkdir /var/lib/prometheus
Set the ownership of the /var/lib/prometheus directory:

 sudo chown prometheus:prometheus /var/lib/prometheus
Pull down the tar.gz file from the Prometheus downloads page:

 cd /tmp/
 wget https://github.com/prometheus/prometheus/releases/download/v2.7.1/prometheus-2.7.1.linux-amd64.tar.gz
Extract the files:

 tar -xvf prometheus-2.7.1.linux-amd64.tar.gz
Move the configuration file and set the owner to the prometheus user:

 sudo mv console* /etc/prometheus
 sudo mv prometheus.yml /etc/prometheus
 sudo chown -R prometheus:prometheus /etc/prometheus
Move the binaries and set the owner:

 sudo mv prometheus /usr/local/bin/
 sudo mv promtool /usr/local/bin/
 sudo chown prometheus:prometheus /usr/local/bin/prometheus
 sudo chown prometheus:prometheus /usr/local/bin/promtool
Create the service file:

 sudo $EDITOR /etc/systemd/system/prometheus.service
Add:

 [Unit]
 Description=Prometheus
 Wants=network-online.target
 After=network-online.target

 [Service]
 User=prometheus
 Group=prometheus
 Type=simple
 ExecStart=/usr/local/bin/prometheus \
     --config.file /etc/prometheus/prometheus.yml \
     --storage.tsdb.path /var/lib/prometheus/ \
     --web.console.templates=/etc/prometheus/consoles \
     --web.console.libraries=/etc/prometheus/console_libraries

 [Install]
 WantedBy=multi-user.target
Save and exit.

Reload systemd:

 sudo systemctl daemon-reload
Start Prometheus, and make sure it automatically starts on boot:

 sudo systemctl start prometheus
 sudo systemctl enable prometheus
 systemctl status prometheus
 
 
 #################################################
 ######################################################
 
 Create the alertmanager system user:

 sudo useradd --no-create-home --shell /bin/false alertmanager
Create the /etc/alertmanager directory:

 sudo mkdir /etc/alertmanager
Download Alertmanager from the Prometheus downloads page:

 cd /tmp/
 wget https://github.com/prometheus/alertmanager/releases/download/v0.16.1/alertmanager-0.16.1.linux-amd64.tar.gz
Extract the files:

 tar -xvf alertmanager-0.16.1.linux-amd64.tar.gz
Move the binaries:

 sudo mv alertmanager /usr/local/bin/
 sudo mv amtool /usr/local/bin/
Set the ownership of the binaries:

 sudo chown alertmanager:alertmanager /usr/local/bin/alertmanager
 sudo chown alertmanager:alertmanager /usr/local/bin/amtool
Move the configuration file into the /etc/alertmanager directory:

 sudo mv alertmanager.yml /etc/alertmanager/
Set the ownership of the /etc/alertmanager directory:

 sudo chown -R alertmanager:alertmanager /etc/alertmanager/
Create the alertmanager.service file for systemd:

 sudo $EDITOR /etc/systemd/system/alertmanager.service

 [Unit]
 Description=Alertmanager
 Wants=network-online.target
 After=network-online.target

 [Service]
 User=alertmanager
 Group=alertmanager
 Type=simple
 WorkingDirectory=/etc/alertmanager/
 ExecStart=/usr/local/bin/alertmanager \
     --config.file=/etc/alertmanager/alertmanager.yml

 [Install]
 WantedBy=multi-user.target
Save and exit.

Stop Prometheus, and then update the Prometheus configuration file to use Alertmanager:

sudo systemctl stop prometheus
sudo $EDITOR /etc/prometheus/prometheus.yml

alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - localhost:9093
Reload systemd, and then start the prometheus and alertmanager services:

sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl start alertmanager
Make sure alertmanager starts on boot:

sudo systemctl enable alertmanager
 
 
 
 #########################################################
 #################### NODE EXPORTER
 ############################################################################
 
 
 
 
 
 
 Create a system user:

 $ sudo useradd --no-create-home --shell /bin/false node_exporter
Download the Node Exporter from Prometheus's download page:

 $ cd /tmp/ && wget https://github.com/prometheus/node_exporter\
 /releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
Extract its contents:

 $ tar -xvf /releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
Move into the newly created directory:

 $ cd node_exporter-0.17.0.linux-amd64/
Move the provided binary:

 $ sudo mv node_exporter /usr/local/bin/
Set the ownership:

 $ sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter
Create a systemd service file:

 $ sudo $EDITOR /etc/systemd/system/node_exporter.service

 [Unit]
 Description=Node Exporter
 After=network.target

 [Service]
 User=node_exporter
 Group=node_exporter
 Type=simple
 ExecStart=/usr/local/bin/node_exporter

 [Install]
 WantedBy=multi-user.target
Save and exit when done.

Start the Node Exporter:

 $ sudo systemctl daemon-reload
 $ sudo systemctl start node_exporter
Add the endpoint to the Prometheus configuration file:

 $ sudo $EDITOR /etc/prometheus/prometheus.yml

   - job_name: 'node_exporter'
     static_configs:
     - targets: ['localhost:9100']:wq
	 
Restart Promtheus:

$ sudo systemctl restart prometheus
Navigate to the Prometheus web UI. Using the expression editor, search for cpu, meminfo, and related system terms to view the newly added metrics.

Search for node_memory_MemFree_bytes in the expression editor; shorten the time span for the graph to be about 30 minutes of data.

Back on the terminal, download and run stress to cause some memory spikes:

$ sudo apt-get install stress
$ stress -m 2
 
 
 http://192.168.1.2:9100
 
 http://192.168.1.2:9090/graph 
 
 
 
 # Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.

    static_configs:
    - targets: ['localhost:9090']

  # - job_name: 'grafana'
   #   static_configs:
    #  - targets: ['localhost:3000']
   - job_name: 'alertmanager'
     static_configs:
     - targets:['localhost:9093']

   - job_name: 'node_exporter'
     static_configs:
     - targets: ['localhost:9100']


 
 
 