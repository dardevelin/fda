__module_name__ = "FDA - Freedom Alert"
__module_version__ = "1.0"
__module_description__ = "Freedom Alert, auto replies each time freedom is mentioned"
__module_author__ = "Darcy 'dardevelin' Bras da Silva"

import hexchat

def fda_print(userdata):
    hexchat.prnt("FDA sent :DID SOMEBODY SAY FREEDOM ?")

def freedom_alert_cb(word, word_eol, userdata):
    #optimize, if there is no f nor F no need to compute lower case
    if 0 == word_eol[1].find('f') and 0 == word_eol[1].find('F'):
        return hexchat.EAT_NONE

    internal = word_eol[1].lower()
    if "freedom" in internal:
        hexchat.command("MSG {} DID SOMEBODY SAY FREEDOM ?".format(hexchat.get_info("channel")))
        hexchat.hook_timer(1000, fda_print)

    return hexchat.EAT_NONE


def unload_cb(userdata):
    print "\0034",__module_name__, __module_version__,"has been unloaded\003"

def on_init_cb():
    hexchat.hook_print("Channel Message", freedom_alert_cb)
    hexchat.hook_unload(unload_cb)
    print "\0034",__module_name__, __module_version__,"has been loaded\003"

on_init_cb()
