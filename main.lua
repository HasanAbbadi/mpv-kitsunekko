local utils = require('mp.utils')

function down_subs()
  mp.msg.warn('Kitsunekko Searching...')
  mp.command('show-text "Kitsunekko Searching..."')

  pyname = '~/.config/mpv/scripts/kitsu/kitsu.py'
  current_file =  mp.get_property("path");

  -- for Mac change python3 to python or pythonw
  start_command = 'python3 "%s" "%s"'
  start = start_command:format(pyname:gsub('~', os.getenv('HOME')), current_file)
  os.execute(start)
  mp.command('show-text "Kitsunekko Finished."')
  mp.commandv("rescan_external_files", "reselect")
end;

mp.add_key_binding("Ctrl+k", "auto_load_subs", down_subs)
