#!/usr/bin/env bash

for TARGETHOST in pslchi6psparel0 svlchi6dkevinl pslchi6ddevl
do
  COUNT=$(echo ${TARGETHOST} | grep -c -E '^[ps][sv]lchi6[sd].*')
  if [[ $COUNT -gt 0 ]]
  then
    printf "${TARGETHOST} "
  fi
done
