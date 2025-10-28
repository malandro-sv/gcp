#!/bin/bash                                                                                                                                                                                                          
                                                                                                                                                                                                                     
#filename=$1 
#zone=$2
#create_instance() {                                                                                                                                                                                                  
#        gcloud compute instances create $MACHINE \
#                --zone=$zone		\
#                --tags=network-lb-tag	\
#                --machine-type=e2-small	\
#                --image-family=debian-12	\
#                --image-project=debian-cloud	\
#                --metadata=startup-script='#!/bin/bash  \                                                                                                                                                            
#                                        apt-get update  \                                                                                                                                                            
#                                        apt-get install apache2 -y \                                                                                                                                                 
#                                        service apache2 restart \                                                                                                                                                    
#                                        echo "<h3>Web Server: $(MACHINE)</h3>: | tee /var/www/html/index.html'                                                                                                       
#};                                                                                                                                                                                   
#                                                                                                                                                                                                                     
#create_loop() {
#        while read MACHINE; do
#		echo "*** Attempting to provision $MACHINE... ***"
#                create_instance $MACHINE
#		echo 
#
#        done < $filename;
#};
#
#
#gcloud compute firewall-rules create www-firewall-network-lb \
#	--target-tags network-lb-tag \
#	--allow tcp:80
# create_loop;
#
declare -a ips=$(gcloud compute instances list | grep -i internal_ip | awk '{print $2}')
for ip in ${ips[@]}; do echo $ip ; done

