'''net_set.py imports functions from net_gargoyle.py to create a new gargoyle.db and nethash table then insert current state.'''
import net_gargoyle as ngr

ngr.createtable()
ngr.interact()
ngr.insertstat()
