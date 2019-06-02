from mcstatus import MinecraftServer

def status(ip):
    """Returns the status of a Minecraft Server.
    Returns None if not reachable.
    """
    server = MinecraftServer.lookup(ip)
    try:
        status = server.status()
        return status
    except:
        return None

def clean_motd(motd, escape_char='§'):
    """Removes color formatting characters from
    message of the day string.

    >>> clean_motd("§8§lServer §2Message")
    'Server Message'
    >>> clean_motd("Server Message")
    'Server Message'
    >>> clean_motd("Server Message§")
    'Server Message'
    """
    if not escape_char in motd:
        return motd

    escape_index = motd.index(escape_char)
    if escape_index == 0:
        return clean_motd(motd[2:], escape_char=escape_char)
    return motd[:escape_index] + clean_motd(motd[escape_index:], escape_char=escape_char)
