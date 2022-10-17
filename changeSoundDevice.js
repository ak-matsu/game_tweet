//https://jutememo.blogspot.com/2012/08/windows.html
  
var wait = function(title){
    do {
	WScript.Sleep(100);
    } while(!WshShell.AppActivate(title));
};

var WshShell =  WScript.CreateObject("WScript.Shell");
WshShell.Run("control mmsys.cpl");
wait("サウンド")
WshShell.SendKeys("{DOWN " + 
	WScript.Arguments.item(0) +
	"}%{s}{TAB 3}{ENTER}");