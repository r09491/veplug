alias tail_victron_mppt_latest="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_latest_\$(date +%y%m%d).log"

alias tail_victron_mppt_watts="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_watts_\$(date +%y%m%d).log"

alias tail_victron_mppt_watt_hours="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_watt_hours_\$(date +%y%m%d).log"


alias show_victron_mppt_volts="tail -n 11 \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_latest_\$(date +%y%m%d).log | \
      				     awk '{print \$1,\$2,\$5}' | sed s/[VAW]//g | \
			    	     termgraph --suffix 'V' --color {blue,red} \
			    	      	       --title 'Victron MPPT latest Volts (SOLAR, BAT)'"		      

alias show_victron_mppt_watts="tail -n 5 \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_watts_\$(date +%y%m%d).log | \
      			    awk '{ print \$2, \$4, \$7, \$10}' |
			    termgraph --color {blue,red,green} --suffix 'W' \
			    	      --title 'Victron MPPT Watts (SOLAR, BAT, LOAD)'"

alias show_victron_mppt_watt_hours="tail -n 5 \$VICTRON_PLUG_STORE_DIR/victron_plug_mppt_watt_hours_\$(date +%y%m%d).log | \
      			    awk '{ print \$2, \$4, \$7, \$10}' |
			    termgraph --color {blue,red,green} --suffix 'Wh' \
			    	      --title 'Victron MPPT Watt-Hours (SOLAR, BAT, LOAD)'"


