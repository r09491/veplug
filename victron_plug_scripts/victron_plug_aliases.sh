# To run in interactive shells VICTRON_PLUG_STORE_DIR is defined in '.bashrc'

alias tail_victron_latest="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_latest_\$(date +%y%m%d).log"

alias tail_victron_watts="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_watts_\$(date +%y%m%d).log"

alias tail_victron_watt_hours="tail -f \$VICTRON_PLUG_STORE_DIR/victron_plug_watt_hours_\$(date +%y%m%d).log"


alias victron_volts="tail -n 11 \$VICTRON_PLUG_STORE_DIR/victron_plug_latest_\$(date +%y%m%d).log | \
      				     awk '{print \$1,\$2,\$5}' | sed s/[VAW]//g | \
			    	     termgraph --suffix 'V' --color {blue,red} \
			    	      	       --title 'Victron MPPT latest Volts (SOLAR, BAT)'"		      

alias victron_watts="tail -n 5 \$VICTRON_PLUG_STORE_DIR/victron_plug_watts_\$(date +%y%m%d).log | \
      			    awk '{ print \$2, \$4, \$7, \$10, \$13}' |
			    termgraph --color {blue,red,green,yellow} --suffix 'W' \
			    	      --title 'Victron MPPT Watts (SOLAR, BAT, LOAD, SYS)'"

alias victron_watt_hours="tail -n 5 \$VICTRON_PLUG_STORE_DIR/victron_plug_watt_hours_\$(date +%y%m%d).log | \
      			    awk '{ print \$2, \$4, \$13, \$16, \$19}' |
			    termgraph --color {blue,red,green,yellow} --suffix 'Wh' \
			    	      --title 'Victron MPPT Watt-Hours (SOLAR, BAT, LOAD, SYS)'"


