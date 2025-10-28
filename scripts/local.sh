#! /bin/bash
#

set_region () {
    read -r -p "set Region: " REGION; export REGION
};

set_val() {
    #read -r -p "Set $1: " $1; export $1
    declare -gx "$1=$2"
}
#gcloud config set account $ACCOUNT;
#gcloud config set project $PROJECT;

