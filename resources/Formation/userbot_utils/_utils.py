#   Med - Userbot
#   Med - Utils

import asyncio
import datetime
import importlib
import inspect
import logging
import math
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from userbot import (
    CMD_HELP, 
    CMD_LIST,
    LOAD_PLUG,
    LOGS, 
    SUDO_LIST,
    usr,
    adn,
    ani,
    tsh,
    ast,
    pmt,
    bot
)
from userbot.Config import Config
from userbot.helpers.progress import CancelProcess


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% usr + shortname)
    else:
        import userbot.utils

        from userbot.helpers.tools import media_type
        from userbot.helpers.utils import (
            _format,
            _icsstools,
            _icssutils,
            install_pip,
            reply_id,
        )
        from userbot.tosh import edit_delete, edit_or_reply

        path = Path(f"userbot/plugins/{shortname}.py")
        name = "userbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = bot.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.rd = reply_id
        mod.admin_cmd = admin_cmd
        mod.zelzal_cmd = admin_cmd
        mod._icssutils = _icssutils
        mod.icut = _icssutils
        mod._icsstools = _icsstools
        mod.icto = _icsstools
        mod.asst_cmd = asst_cmd
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.ed = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = userbot.utils
        mod.borg = bot
        mod.Rallsthonbot = bot
        mod.Rallsthon = bot
        # support for paperplaneextended
        sys.modules["userbot.events"] = userbot.utils
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["userbot.plugins." + shortname] = mod
        print('%s'% usr + shortname)

def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"userbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

def admin_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        else:
            if len(Config.COMMAND_HAND_LER) == 2:
                icsreg = "^" + Config.COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER[1]
            elif len(Config.COMMAND_HAND_LER) == 1:
                icsreg = "^\\" + Config.COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER
            args["pattern"] = re.compile(icsreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if black_list_chats:
        args["chats"] = black_list_chats

    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'

    return events.NewMessage(**args)


def sudo_cmd(pattern=None, command=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith(r"\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
        else:
            if len(Config.SUDO_COMMAND_HAND_LER) == 2:
                catreg = "^" + Config.SUDO_COMMAND_HAND_LER
                reg = Config.SUDO_COMMAND_HAND_LER[1]
            elif len(Config.SUDO_COMMAND_HAND_LER) == 1:
                catreg = "^\\" + Config.SUDO_COMMAND_HAND_LER
                reg = Config.COMMAND_HAND_LER
            args["pattern"] = re.compile(catreg + pattern)
            if command is not None:
                cmd = reg + command
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                SUDO_LIST[file_test].append(cmd)
            except BaseException:
                SUDO_LIST.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]
    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if black_list_chats:
        args["chats"] = black_list_chats
    # add blacklist chats, UB should not respond in these chats
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]
    # check if the plugin should listen for outgoing 'messages'
    return events.NewMessage(**args)


def errors_handler(func):
    async def wrapper(errors):
        try:
            await func(errors)
        except BaseException:
            if Config.PRIVATE_GROUP_BOT_API_ID != 0:
                return
            date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            ftext = "\nDisclaimer:\nThis file is pasted only here ONLY here,"
            ftext += "\nwe logged only fact of error and date,"
            ftext += "\nwe respect your privacy,"
            ftext += "\nyou may not report this error if you've"
            ftext += "\nany confidential data here, no one will see your data\n\n"
            ftext += "--------BEGIN Ralls TRACEBACK LOG--------"
            ftext += "\nDate: " + date
            ftext += "\nGroup ID: " + str(errors.chat_id)
            ftext += "\nSender ID: " + str(errors.sender_id)
            ftext += "\n\nEvent Trigger:\n"
            ftext += str(errors.text)
            ftext += "\n\nTraceback info:\n"
            ftext += str(traceback.format_exc())
            ftext += "\n\nError text:\n"
            ftext += str(sys.exc_info()[1])
            new = {"error": str(sys.exc_info()[1]), "date": datetime.datetime.now()}
            ftext += "\n\n--------END Ralls TRACEBACK LOG--------"

            command = 'git log --pretty=format:"%an: %s" -5'

            ftext += "\n\n\nLast 5 commits:\n"

            process = await asyncio.create_subprocess_shell(
                command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            result = str(stdout.decode().strip()) + str(stderr.decode().strip())
            ftext += result
            from .helpers.utils import _format

            pastelink = _format.paste_text(ftext)
            text = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝗠𝗘𝗗𝗧𝗵𝗼𝗻 𝑬𝑹𝑹𝑶𝑹 𝑹𝑬𝑷𝑶𝑹𝑻 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝗠𝗘𝗗𝗧𝗵𝗼𝗻ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n"
            link = "[مطور السـورس](https://t.me/L_U_2)"
            text += "- إذا كنت تريد أن تتمكن من الإبلاغ عن المشكله"
            text += f"- فقط قم بتوجيه هذا الرساله الى {link}.\n"
            text += "- لا يوجد شيء مسجل باستثناء حقيقة الخطأ والتاريخ\n\n"
            text += f"**- الابلاغ عن الخطا : ** [{new['error']}]({pastelink}) \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
            await errors.client.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
            )

    return wrapper


async def progress(
    current, total, event, start, type_of_ps, file_name=None, is_cancelled=None
):
    now = time.time()
    diff = now - start
    if is_cancelled is True:
        raise CancelProcess
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}] {2}%\n".format(
            "".join("▰" for i in range(math.floor(percentage / 10))),
            "".join("▱" for i in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )

        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            await event.edit(
                "{}\nFile Name: `{}`\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def human_to_bytes(size: str) -> int:
    units = {
        "M": 2 ** 20,
        "MB": 2 ** 20,
        "G": 2 ** 30,
        "GB": 2 ** 30,
        "T": 2 ** 40,
        "TB": 2 ** 40,
    }

    size = size.upper()
    if not re.match(r" ", size):
        size = re.sub(r"([KMGT])", r" \1", size)
    number, unit = [string.strip() for string in size.split()]
    return int(float(number) * units[unit])


# Inputs time in milliseconds, to get beautified time, as string
def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


class Loader:
    def __init__(self, func=None, **args):
        self.Config = Config
        bot.add_event_handler(func, events.NewMessage(**args))


# Admin checker by uniborg
async def is_admin(client, chat_id, user_id):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await client(GetParticipantRequest(channel=chat_id, user_id=user_id))
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False


def register(**args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    disable_edited = args.get("disable_edited", True)
    allow_sudo = args.get("allow_sudo", False)

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    if "disable_edited" in args:
        del args["disable_edited"]

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass

            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass

    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def command(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    pattern = args.get("pattern", None)
    allow_sudo = args.get("allow_sudo", None)
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass
    if allow_sudo:
        args["from_users"] = list(Config.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
    del allow_sudo
    try:
        del args["allow_sudo"]
    except BaseException:
        pass

    args["blacklist_chats"] = True
    black_list_chats = list(Config.UB_BLACK_LIST_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if "allow_edited_updates" in args:
        del args["allow_edited_updates"]

    def decorator(func):
        if allow_edited_updates:
            bot.add_event_handler(func, events.MessageEdited(**args))
        bot.add_event_handler(func, events.NewMessage(**args))
        try:
            LOAD_PLUG[file_test].append(func)
        except BaseException:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


# For dmain 
def load_admin(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/Admin/{shortname}.py")
        name = "userbot.plugins.Admin.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% adn + shortname)

    else:
        import userbot.utils

        from userbot.helpers.tools import media_type
        from userbot.helpers.utils import (
            _format,
            _icsstools,
            _icssutils,
            install_pip,
            reply_id,
        )
        from userbot.tosh import ed, eor

        path = Path(f"userbot/plugins/Admin/{shortname}.py")
        name = "userbot.plugins.Admin.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.Config = Config
        mod.tgbot = bot.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.rd = reply_id
        mod.admin_cmd = admin_cmd
        mod.zelzal_cmd = admin_cmd
        mod.ed = ed
        mod.edit_delete = ed
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        mod.Rallsthonbot = bot
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.Admin." + shortname] = mod
        print('%s'% adn + shortname)


# For animations
def load_anim(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/animations/{shortname}.py")
        name = "userbot.plugins.animations.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% ani + shortname)
    else:
        import userbot.utils
        from userbot.tosh import ed, eor

        path = Path(f"userbot/plugins/animations/{shortname}.py")
        name = "userbot.plugins.animations.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.Config = Config
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.admin_cmd = admin_cmd
        mod.eor = eor
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        mod.Rallsthonbot = bot
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.animations." + shortname] = mod
        print('%s'% ani + shortname)

# For Gif 
def load_tosha(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/tosha/{shortname}.py")
        name = "userbot.plugins.tosha.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% tsh + shortname)
    else:
        import userbot.utils

        from userbot.helpers.utils import reply_id
        from userbot.tosh import ed, eor

        path = Path(f"userbot/plugins/tosha/{shortname}.py")
        name = "userbot.plugins.tosha.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.sudo_cmd = sudo_cmd
        mod.reply_id = reply_id
        mod.rd = reply_id
        mod.admin_cmd = admin_cmd
        mod.zelzal_cmd = admin_cmd
        mod.ed = ed
        mod.edit_delete = ed
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        mod.Rallsthonbot = bot
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.tosha." + shortname] = mod
        print('%s'% tsh + shortname)

# for assistant 

import functools
from telethon import events

bothandler = Config.BOT_HANDLER

def asst_cmd(dec):
    def kim(func):
        pattern = dec
        bot.tgbot.add_event_handler(
            func, events.NewMessage(incoming=True, pattern=pattern)
        )

    return kim

def owner():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            Kud = Config.OWNER_ID
            if event.sender_id == Kud:
                await func(event)
            else:
                pass

        return wrapper

    return decorator

# for assistant
def load_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/assistant/{shortname}.py")
        name = "userbot.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% ast + shortname)
    else:
        import userbot.utils
        from userbot.helpers.utils import _format

        path = Path(f"userbot/plugins/assistant/{shortname}.py")
        name = "userbot.plugins.assistant.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.Config = Config
        mod.tgbot = bot.tgbot
        mod._format = _format
        mod.asst_cmd = asst_cmd
        mod.owner = owner()
        mod.asst = bot.tgbot
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        mod.borg = bot
        sys.modules["userbot.events"] = userbot.utils
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins." + shortname] = mod
        print('%s'% ast + shortname)

# Asstistamt pm
def load_asstpm(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/plugins/assistant/PmTosh/{shortname}.py")
        name = "userbot.plugins.assistant.PmTosh.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print('%s'% pmt + shortname)
    else:
        import userbot.utils
        from userbot.helpers.utils import _format

        path = Path(f"userbot/plugins/assistant/PmTosh/{shortname}.py")
        name = "userbot.plugins.assistant.PmTosh.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod._format = _format
        mod.asst_cmd = asst_cmd
        mod.asst = bot.tgbot
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        sys.modules["userbot.events"] = userbot.utils
        mod.owner = owner()
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.assistant.PmTosh" + shortname] = mod
        print('%s'% pmt + shortname)

# ==============
# Med - Userbot: Utils end
