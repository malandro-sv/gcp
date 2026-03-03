#! /bin/bash
#

set_region () {
    read -r -p "set Region: " REGION; export REGION
};

set_val() {
    #TODO: build another procedure to
    # take set_val args and pass them to
    #gcloud config set account $ACCOUNT;
    #gcloud config set project $PROJECT;
    #read -r -p "Set $1: " $1; export $1
    declare -gx "$1=$2"
}

