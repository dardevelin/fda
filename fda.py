__module_name__ = "FDA - Freedom Alert"
__module_version__ = "1.1"
__module_description__ = "Freedom Alert, auto replies each time freedom is mentioned"
__module_author__ = "Darcy 'dardevelin' Bras da Silva"

import hexchat
#None, True, False
fda_status = None

def fda_print(userdata):
    hexchat.emit_print("Channel Message",hexchat.get_info("nick"), "DID SOMEBODY SAY FREEDOM ?","@")

def freedom_alert_cb(word, word_eol, userdata):
    global fda_status
    if fda_status == False:
        return hexchat.EAT_NONE

    #optimize, if there is no f nor F no need to compute lower case
    if 0 == word_eol[1].find('f') and 0 == word_eol[1].find('F'):
        return hexchat.EAT_NONE

    internal = word_eol[1].lower()
    if "freedom" in internal:
        nickname = hexchat.get_info("nick")
        if hexchat.nickcmp(nickname, word[0]) != 0:
            hexchat.command("MSG {} DID SOMEBODY SAY FREEDOM ?".format(hexchat.get_info("channel")))
            hexchat.hook_timer(500, fda_print)

    return hexchat.EAT_NONE

def unload_cb(userdata):
    print "\0034",__module_name__, __module_version__,"has been unloaded\003"

def toggle_fda(word, word_eol, userdata):
    global fda_status

    if fda_status == True:
        fda_status = False
    else:
        fda_status = True

    if fda_status == True:
        hexchat.prnt("FDA is now at full speed")
    else:
        hexchat.prnt("FDA is now suspended")

def on_init_cb():
    global fda_status
    fda_status = True
    hexchat.hook_print("Channel Message", freedom_alert_cb)
    hexchat.hook_unload(unload_cb)
    hexchat.hook_command("fda", toggle_fda)
    print "\0034",__module_name__, __module_version__,"has been loaded\003"

on_init_cb()
