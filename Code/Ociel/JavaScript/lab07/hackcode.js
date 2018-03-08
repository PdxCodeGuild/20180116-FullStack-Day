let hackcode = `myHostname = window.location.hostname;

var myTLD = "." + myHostname.substring(myHostname.indexOf("wupload") + 
"wupload.".length).split(".")[0];

function afterLoad() {

  return

}

ieFixForFileSelectionOnChangeEventTimer = null;




function ieFixForFileSelectionOnChangeEvent(a) {

  $("#siteName").toggle();

  if ($("#inputFileSelection").val() == "") {

    ieFixForFileSelectionOnChangeEventTimer = 
setTimeout("ieFixForFileSelectionOnChangeEvent()", 200)

  } else {

    $("body")[0].focus()

  }

}

function urlencode(a) {

  return escape(a.toString().replace(/%/g, "%25").replace(/+/g, 
"%2B")).replace(/%25/g, "%")

}

$(document).ajaxStart(function() {

  $("body").addClass("ajaxLoading")

});

$(document).ajaxStop(function() {

  $("body").removeClass("ajaxLoading")

});

$(document).ajaxError(function(d, c, a, b) {

  CMApplication.Widgets.Dialog.close();

  CMApplication.Widgets.Dialog.displayMessage(c.responseText, 
CMApplication.Widgets.Dialog.Types.exception)

});

jQuery.setCookie = function(b, c, a) {

  var d = new Date();

  d.setDate(d.getDate() + a);

  cookieDomain = ".wupload" + myTLD;

  document.cookie = b + "=" + escape(c) + ((a == null) ? "" : ";expires=" + 
d.toUTCString() + "; path=/;domain=" + cookieDomain + ";")

};

jQuery.getCookie = function(a) {

  if (document.cookie.length > 0) {

    c_start = document.cookie.indexOf(a + "=");

    if (c_start != -1) {

      c_start = c_start + a.length + 1;

      c_end = document.cookie.indexOf(";", c_start);

      if (c_end == -1) {

        c_end = document.cookie.length

      }

      return unescape(document.cookie.substring(c_start, c_end))

    }

  }

  return ""

};

jQuery.unparam = function(d) {

  var f = {},

    c = d.split("&"),

    e, b, a;

  for (b = 0, a = c.length; b < a; b++) {

    e = c[b].split("=", 2);

    f[decodeURIComponent(e[0])] = (e.length == 2 ? 
decodeURIComponent(e[1].replace(/+/g, " ")) : true)

  }

  return f

};

CMApplication = {

  User: {

    RolesNames: ["anonymous", "free", "premium"],

    RolesValues: {

      ANONYMOUS: 0,

      FREE: 1,

      PREMIUM: 2

    }, sessId: "",

    email: "",

    isAffiliate: false,

    role: "anonymous"

  }, Bootstrap: {

    run: function() {

      for (var a in this) {

        if (a.indexOf("_init") === -1) {

          continue

        }

        this[a]()

      }

      CMApplication.Widgets.Ajax._init()

    }

  }, Dictionnary: {

    SEARCH_ALL_FOLDERS: "Search all folders:",

    SEARCH_THIS_FOLDERS: "Search this folders:",

    PLEASE_WAIT: "Please Wait...",

    SHARE: "Share",

    SHARE_FILES: "Share Files",

    EDIT: "Edit",

    TRASH: "Trash",

    DOWNLOAD_READY: "Download Ready",

    START_DOWNLOAD_NOW: "Start download now!",

    LEAVING_WILL_CANCEL_UPLOADS: "If you continue, your upload(s) will be 
cancelled.",

    YOUR_UPLOADS: "Your uploads",

    COMPLETED: "Completed",

    CLOSE: "Close",

    VIEW_LINKS: "View Links",

    UNEXPECTED_PROCESS_ERROR: "Unexpected error during process",

    LOGIN_UNEXPECTED_PROCESS_ERROR: "Unexpected error during login",

    SYSTEM_ERROR: "System Error",

    ERROR: "Error",

    NOTICE: "Notice",

    FILESYSTEM_MOVE_INSTRUCTION: "Select the file/folder you want to move on the 
right side of the file browser.",

    FILESYSTEM_COPY_INSTRUCTION: "Select the file/folder you want to copy on the 
right side of the file browser.",

    FILESYSTEM_TRASH_INSTRUCTION: "Select the file/folder you want to delete on 
the right side of the file browser.",

    FILESYSTEM_GENERATELINKS_INSTRUCTION: "Select the file(s) you want to generate 
link on the right side of the file browser.",

    FILESYSTEM_PREMIUM_INSTRUCTION: "Select the file(s) you want to set only for 
premium on the right side of the file browser.",

    FOLDER_ID_REQUIRED: "Folder ID should be specified",

    FILESYSTEM_MOVE_SOURCE_IDENTICAL_TO_DESTINATION: "Impossible to move: The 
source folder is identical then the destination",

    FILESYSTEM_MOVE_DESTINATION_SUBFOLDER_OF_SOURCE: "Impossible to move: The 
destination folder is a subfolder of the source.",

    FILESYSTEM_MOVE_UNABLE_TO_MOVE: "Unable to move selected file/folder",

    FILESYSTEM_COPY_UNABLE_TO_COPY: "Unable to copy selected file/folder",

    FILESYSTEM_TRASH_UNABLE_TO_TRASH: "Unable to trash selected file/folder",

    FILESYSTEM_PREMIUM_UNABLE_TO_PREMIUM: "Unable to set only for premium selected 
file(s)",

    COPY_FOLDER_NOT_YET_IMPLEMENTED: "Copy of folder not yet implemented",

    PAGE_SHOULD_BE_OPENED_IN_NEW_WINDOW: "For technical reasons, this page should 
be opened in a new window/tab when uploading a file.",

    USER_HAS_TO_WAIT: "User has to wait",

    VIEW_ALL_LINKS: "View all links",

    SELECT_A_DESTINATION: "Select a destination",

    MOVE: "Move",

    CANCEL: "Cancel",

    CANCEL_UPLOAD: "Cancel Upload",

    ARE_YOU_SURE_YOU_WANT_TO_DELETE_THESE_FILES: "Are you sure you want to delete 
these files / folder ?",

    ARE_YOU_SURE_YOU_WANT_TO_SET_THESE_FILES_ONLY_PREMIUM: "Are you sure you want 
to set these files only for premium?",

    ARE_YOU_SURE_YOU_WANT_TO_UNSET_THESE_FILES_ONLY_PREMIUM: "Are you sure you 
want to unset these files only for premium?",

    DESCRIPTION: "Description:",

    IS_PUBLIC: "Is Public:",

    LINK: "Link",

    LINKS: "Links:",

    DATE_CREATED: "Created On:",

    DATE_UPDATED: "Updated On:",

    MUST_BE_PUBLIC: "Must be public",

    COPY: "Copy",

    REMOTE_UPLOAD: "Remote Upload",

    WEB_UPLOAD: "Web Upload",

    UNKNOWN: "Unknown",

    SIZE: "Size",

    SOURCE: "Source",

    PASSWORD: "Password",

    PREMIUM_ONLY: "Premium Only",

    TOTAL_SIZE: "Total Size:",

    FOLLOWING_ERROR_DURING_UPLOAD: "The following errors happen during the 
upload:",

    RENAME: "Rename",

    UPLOADING: "Uploading",

    FILES: "Files",

    RESTORE: "Restore",

    SELECT: "Select",

    MINIMIZE: "Minimize",

    FILES_UPLOADED_TO: "Files uploaded to:",

    CHOOSE_FILES_TO_UPLOAD: "Choose files to upload",

    UPLOAD_NOW: "Upload Now",

    YOU_SUCCESSFULLY_UPLOADED: "You successfully uploaded",

    YOU_UPLOADED: "You uploaded",

    ERROR_DURING_THE_UPLOAD: "Error during the upload",

    SHARE_ALL_LINKS: "Share ALL Links",

    CHOOSE_FILES_AND_THEN_PRESS_UPLOAD_NOW: "Choose files to upload, then click 
&quot;Start Upload&quot;",

    TOTAL_FILES: "Total Files:",

    FILE_NAME: "File name",

    PROGRESS: "Progress",

    DOWNLOAD_LINK: "Download Link",

    FAIL: "Fail",

    VIEW_LINK: "View Link",

    START_UPLOAD: "Start Upload",

    SELECTABLE: "Selectable"

  }, URLs: {

    languageFilesystemExportFolderLinks: "/file-manager/export-all-
links/:folderId",

    languageFilesystemCopy: "/file-manager/copy/:id",

    languageFilesystemMove: "/file-manager/move/:id",

    languageFilesystemEditMultiple: "/file-manager/edit-files/:id",

    languageFilesystemShare: "/file-manager/share/email/:ids",

    languageFilesystemEdit: "/file-manager/edit/:id",

    languageFilesystemCreate: "/file-manager/create/:parentId",

    languageFilesystemTrash: "/file-manager/delete/:id",

    languageFilesystemGenerateLink: "/file-manager/share/urls/:id",

    languageFilesystemBrowse: "/file-
manager/list/:folderId/:page/:orderBy/:orderDirection/:globalSearch/:queryString",

    languageFilesystemRemoved: "/file-manager/removed",

    languageDownload: "/file/:id",

    uploadProgress: 
":hostserver/nginxuploadprogress?unique=:unique&ID=:progress_key&X-Progress-
ID=:progress_key",

    uploadCallback: "/upload/done/:uploadProgressId",

    domain: "http://" + window.location.host

  }, foward: function(a) {

    location.href = a

  }, Viewport: {

    width: null,

    height: null,

    adjust: function() {

      if (typeof window.innerWidth != "undefined") {

        this.width = window.innerWidth,

        this.height = window.innerHeight

      } else {

        if (typeof document.documentElement != "undefined" && typeof 
document.documentElement.clientWidth != "undefined" && 
document.documentElement.clientWidth != 0) {

          this.width = document.documentElement.clientWidth,

          this.height = document.documentElement.clientHeight

        } else {

          this.width = document.getElementsByTagName("body")[0].clientWidth,

          this.height = document.getElementsByTagName("body")[0].clientHeight

        }

      }

      var a = false;

      if (navigator.userAgent.indexOf("MSIE 6") != -1) {

        a = true

      }

    }

  }, Layout: {

    _init: function() {

      if (CMApplication.User.email != "") {

        $("body").addClass("loggedIn")

      } else {

        $("body").removeClass("loggedIn")

      }

      $("#lMainUsage a[href=" + window.location + 
"]").parent("li").addClass("active");

      $("#lMainUsage li.active").parent("li").addClass("active");

      $("#lMainUsage li.active").parent("ul").parent("li").addClass("active");

      $("ul.main li li.account").live("mouseenter", function(a) {

        $(this).addClass("hover");

        $("ul.lMore", this).show()

      });

      $("ul.main li li.account").live("mouseleave", function(a) {

        $(this).removeClass("hover");

        $("ul.lMore", this).hide()

      })

    }

  }, Widgets: {}, Pages: {}

};

sortFolders = function(d, c) {

  var g = $('#sortForm input[name="folder_field"]').val();

  if (g == "name") {

    var f = encodeURI($(d).text()).replace("%0A%20%20%20%20%20%20%20%20", 
"").replace("%0A%20%20%20%20", "");

    var e = encodeURI($(c).text()).replace("%0A%20%20%20%20%20%20%20%20", 
"").replace("%0A%20%20%20%20", "")

  } else {

    if (g == "date") {

      var f = $(d).attr("data-date");

      var e = $(c).attr("data-date")

    }

  }

  if ($('#sortForm input[name="folder_direction"]').val() == "desc") {

    return (f > e) ? -1 : (f < e) ? 1 : 0

  } else {

    return (f < e) ? -1 : (f > e) ? 1 : 0

  }

};

$(document).ready(function() {

  var counter = 0;

  $("#internationalization a.active").click(function() {

    return false

  });

  $("#internationalization").click(function() {

    $("#internationalization li").toggleClass("open").delay(800);

    $("div#internationalization ul").toggleClass("opened").delay(800);

    counter++

  });

  $("html").click(function() {

    if (counter % 2) {

      $("#internationalization li").toggleClass("open").delay(800);

      $("div#internationalization ul").toggleClass("opened").delay(800);

      counter++

    }

  });

  if (jQuery.getCookie("isJavascriptEnable") != 1) {

    jQuery.setCookie("isJavascriptEnable", 1, 30)

  }

  $("#DialogWidget #signupCompleted form").live("successCallback", function(event, 
data) {

    $(this).removeAttr("rel")

  });

  $("#free_download, #free_download2, #cancelDownload").live("click", 
function(event) {

    $("#freeDownload").hide();

    event.preventDefault();

    $.post(this.href, $("#downloadMode form").serialize(), function(data) {

      $("#premiumDownload").remove();

      $("#downloadMode").replaceWith(data);

      $("#downloadMode").slideDown("slow")

    })

  });

  $("#downloadMode form").live("submit", function(event) {

    event.preventDefault();

    $.post(this.action, $("#downloadMode form").serialize(), function(data) {

      $("#downloadMode").replaceWith(data);

      $("#downloadMode").slideDown("slow")

    })

  });

  $('#downloadMode form input[type="submit"], #downloadMode form 
button').live("click", function(event) {

    event.preventDefault();

    $.post($("#downloadMode form").attr("action"), $("#downloadMode 
form").serialize(), function(data) {

      $("#downloadMode").replaceWith(data);

      $("#downloadMode").slideDown("slow")

    })

  });

  isSearchResult = false;

  CMApplication.Widgets.Ajax = {

    Events: {

      click: function(e) {

        if (e.isDefaultPrevented()) {

          return

        }

        var internalLinkRegEx = /^(\\#|\\/|https?\\:\\/\\/([^.]+\\.)?wupload(\\.[a-
z]{2,3})+\\/?)/i;

        destination = $(this).attr("href");

        isInternal = internalLinkRegEx.test(destination);

        var anchorRegEx = /(\\#.*)$/i;

        isAnchor = anchorRegEx.test(destination);

        if (!isInternal) {

          return

        }

        e.preventDefault();

        localPath = 
CMApplication.Widgets.Ajax.getHash(destination).replace(anchorRegEx, "");

        if (localPath != "" && !(localPath == window.location.pathname && 
isAnchor)) {

          var intelligenceRegEx = /\\/intelligence(\\/.*)?$/i;

          isIntelligence = intelligenceRegEx.test(localPath);

          if (!isIntelligence) {

            $.history.load(localPath)

          } else {

            alert(CMApplication.Dictionnary.PAGE_SHOULD_BE_OPENED_IN_NEW_WINDOW);

            window.open(localPath)

          }

        }

        anchor = anchorRegEx.exec(destination);

        if (anchor !== null && $(anchor[0]).length == 1) {

          setTimeout("$('html,body').animate({scrollTop: " + 
$(anchor[0]).offset().top + "}, 800);", 1)

        }

      }, submit: function(e) {

        if (e.isDefaultPrevented()) {

          return

        }

        var internalLinkRegEx = /^(\\#|\\/|https?\\:\\/\\/([^.]+\\.)?wupload(\\.[a-
z]{2,3})+\\/?)/i;

        destination = $(this).attr("action");

        isInternal = internalLinkRegEx.test(destination);

        if (!isInternal) {

          return

        }

        e.preventDefault();

        localPath = CMApplication.Widgets.Ajax.getHash(destination);

        jQuery.ajax({

          url: localPath,

          type: $(this).attr("method") || "get",

          data: $(this).serialize(),

          dataType: "html",

          complete: function(XMLHttpRequest, textStatus) {

            $("#mainContent").html(XMLHttpRequest.responseText)

          }

        })

      }

    }, start: function() {

      alert("Starting Ajax Browsing");

      $("form").live("submit", CMApplication.Widgets.Ajax.Events.submit);

      $("a").live("click", CMApplication.Widgets.Ajax.Events.click);

      $.history.init(function(hash) {

        if (hash == "") {

          url = CMApplication.Widgets.Ajax.getHash(location.href)

        } else {

          jQuery.ajax({

            url: hash,

            async: false,

            global: false,

            type: "get",

            dataType: "html",

            data: {

              isGlobalAjax: "1"

            }, complete: function(XMLHttpRequest, textStatus) {

              $("#mainContent").html(XMLHttpRequest.responseText)

            }

          });

          $("html,body").animate({

            scrollTop: 0

          }, 1)

        }

      }, {

        unescape: ",/"

      })

    }, stop: function() {

      alert("Stopping Ajax Browsing");

      $("form").die("submit", CMApplication.Widgets.Ajax.Events.submit);

      $("a").die("click", CMApplication.Widgets.Ajax.Events.click);

      $.history.init(function() {}, {

        unescape: ",/"

      })

    }, _init: function() {}, getHash: function(url) {

      hostnameRegEx = /^(https?+)/i;

      return url.replace(hostnameRegEx, "")

    }

  };

  CMApplication.Widgets.Purchase = {

    Events: {

      submit: function(e) {

        e.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("action"));

        editForm = $("form", CMApplication.Widgets.Dialog.dialogContainer);

        editForm.bind("successCallback", function(event, data) {

          if (data.data.paymentSystem == 3) {

            $(event.target).attr("rel", "keep");

            $("#DialogWidgetContent").load(data.redirect)

          } else {

            location.href = data.redirect

          }

        });

        editForm.bind("failCallback", function(event, data) {

          $(event.target).attr("rel", "keep")

        })

      }

    }, _init: function() {

      $(".form_payment_system_3, .form_payment_system_8.premiumEmail, 
.form_payment_system_9.premiumEmail").live("submit", 
CMApplication.Widgets.Purchase.Events.submit)

    }

  };

  CMApplication.Widgets.Tools = {

    Events: {

      click: function(e) {

        e.preventDefault();

        $(this).addClass("active");

        $('#lUser li.lMore:not("#statsLinks") ul').show();

        $(document).bind("click", closeUserMenuMore);




        function closeUserMenuMore(e) {

          clickedElement = $(e.target);

          if (!clickedElement.is('#lUser li.lMore:not("#statsLinks") ul') && 
clickedElement.parents('#lUser li.lMore:not("#statsLinks") ul').length < 1) {

            $('#lUser li.lMore:not("#statsLinks") a').removeClass("active");

            $('#lUser li.lMore:not("#statsLinks") ul').hide();

            $(document).unbind("click", closeUserMenuMore)

          }

        }

      }

    }, _init: function() {

      $('#lUser li.lMore:not("#statsLinks") > a:not(.active)').live("click", 
CMApplication.Widgets.Tools.Events.click)

    }

  };

  CMApplication.Widgets.Stats = {

    Events: {

      click: function(e) {

        e.preventDefault();

        $(this).addClass("active");

        $("#lUser li.lMore#statsLinks ul").show();

        $(document).bind("click", closeUserMenuMore);




        function closeUserMenuMore(e) {

          clickedElement = $(e.target);

          if (!clickedElement.is("#lUser li.lMore#statsLinks ul") && 
clickedElement.parents("#lUser li.lMore#statsLinks ul").length < 1) {

            $("#lUser li.lMore#statsLinks a").removeClass("active");

            $("#lUser li.lMore#statsLinks ul").hide();

            $(document).unbind("click", closeUserMenuMore)

          }

        }

      }

    }, _init: function() {

      $("#lUser li.lMore#statsLinks > a:not(.active)").live("click", 
CMApplication.Widgets.Stats.Events.click)

    }

  };

  CMApplication.Pages.Download = {

    PasswordProtection: {

      formElement: $("body#Download_Index #passwordProtection form"),

      Events: {

        submit: function(event) {

          event.preventDefault();

          jQuery.ajax({

            url: $(this).attr("action"),

            type: $(this).attr("method"),

            dataType: "json",

            data: $(this).serialize(),

            success: function(data) {

              if (data.status == "success") {

                jQuery.ajax({

                  url: data.redirect,

                  type: "GET",

                  dataType: "html",

                  success: function(data) {

                    $("#premiumMessages").html(data)

                  }

                })

              } else {

                container = $("#password").parent();

                errorContainer = $("ul.errors", container);

                if (errorContainer.length === 0) {

                  errorContainer = $('<ul class="errors" />').appendTo(container)

                }

                for (fieldName in data.messages) {

                  errors = "";

                  field = data.messages[fieldName];

                  for (error in field) {

                    errors += "<li>" + field[error] + "</li>"

                  }

                  errorContainer.html(errors)

                }

              }

            }

          })

        }

      }

    }, CountDown: {

      delay: 60,

      decrease: function() {

        if (this.delay > 0) {

          this.delay--;

          $("#countdown").text(this.getFormatedDelay());

          window.onPageTimeout = 
setTimeout("CMApplication.Pages.Download.CountDown.decrease();", 1050)

        } else {

          $.post("?start=1", $("#tm, #tm_hash").serialize(), function(data) {

            $("#downloadMode").replaceWith(data)

          })

        }

      },

      hack: function() {

          $.post("?start=1", $("#tm, #tm_hash").serialize(), function(data) {

            $("#downloadMode").replaceWith(data)

          })

      }

      , getFormatedDelay: function() {

        returnValue = this.delay / 60;

        returnValue = returnValue.toString().split(".");

        minutes = returnValue[0];

        seconds = this.delay - (minutes * 60);

        if (seconds.toString().length == 1) {

          seconds = "0" + seconds

        }

        if (minutes < 1) {

          rv = seconds + "s"

        } else {

          rv = minutes + " min."

        }

        return rv

      }

    }, _init: function() {

      CMApplication.Pages.Download.PasswordProtection.formElement.live("submit", 
CMApplication.Pages.Download.PasswordProtection.Events.submit);

      if (typeof(countDownDelay) !== "undefined") {

        CMApplication.Pages.Download.CountDown.delay = countDownDelay;

        CMApplication.Pages.Download.CountDown.decrease();

        try {

          pageTracker._trackEvent("download_delay", "wait_" + countDownDelay, 
CMApplication.Dictionnary.USER_HAS_TO_WAIT + countDownDelay)

        } catch(e) {}

      }

    }

  };

  CMApplication.Widgets.Dialog = {

    dialogContainer: null,

    Types: {

      exception: 1,

      error: 2,

      notice: 3

    }, Events: {

      close: function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.close()

      }, submit: function(event) {

        event.preventDefault();

        var formSubmitted = $(this);

        jQuery.ajax({

          url: formSubmitted.attr("action"),

          data: formSubmitted.serializeArray(),

          type: formSubmitted.attr("method"),

          dataType: "json",

          success: function(data, textStatus, XMLHttpResponse) {

            if (data.status == "success") {

              form = formSubmitted.trigger("successCallback", data)

            } else {

              form = formSubmitted.trigger("failCallback", data);

              if ($(form).attr("rel") == "keep") {

                for (var i in data.messages) {

                  for (var j in data.messages[i]) {

                    message = data.messages[i][j];

                    if ($("#" + 
i).parent("div.elements").children(".errors").length == 0) {

                      $("#" + i).parent("div.elements").append("<ul 
class='errors'><li>" + message + "</li></ul>")

                    } else {

                      $("#" + 
i).parent("div.elements").children(".errors").html("<li>" + message + "</li>")

                    }

                  }

                }

              }

            }

            if ($(form).attr("rel") != "keep") {

              CMApplication.Widgets.Dialog.close()

            }

          }

        })

      }

    }, displayMessage: function(message, type, className, positionTarget) {

      switch (type) {

      case CMApplication.Widgets.Dialog.Types.exception:

        title = CMApplication.Dictionnary.SYSTEM_ERROR;

        lclassName = "systemError";

        break;

      case CMApplication.Widgets.Dialog.Types.error:

        title = CMApplication.Dictionnary.ERROR;

        lclassName = "error";

        break;

      case CMApplication.Widgets.Dialog.Types.notice:

        title = CMApplication.Dictionnary.NOTICE;

        lclassName = "notice";

        break

      }

      html = '<div id="DialogWidgetMessage" class="' + lclassName + '"><h2><span>' 
+ title + "</span></h2>" + message + "</div>";

      CMApplication.Widgets.Dialog.open(html, 400, className, positionTarget)

    }, displayUrl: function(url, width, className, positionTarget) {

      var width;

      ajaxUrl = url;

      jQuery.ajax({

        url: ajaxUrl,

        type: "get",

        dataType: "html",

        async: false,

        success: function(data, textStatus, XMLHttpResponse) {

          CMApplication.Widgets.Dialog.displayContent(data, width, className, 
positionTarget)

        }

      })

    }, displayContent: function(content, width, className, positionTarget) {

      CMApplication.Widgets.Dialog.open(content, width, className, positionTarget)

    }, open: function(content, size, className, positionTarget) {

      if (typeof(size) == "object") {

        if ("undefined" != typeof(size.width)) {

          width = size.width

        } else {

          width = undefined

        }

        if ("undefined" != typeof(size.height)) {

          height = size.height

        } else {

          height = undefined

        }

      } else {

        width = size;

        height = undefined

      }

      if ("undefined" == typeof(className)) {

        className = "defaultStyle"

      }

      dContainer = CMApplication.Widgets.Dialog.dialogContainer;

      if (dContainer == null) {

        CMApplication.Widgets.Dialog._init()

      }

      $("#DialogWidget").attr("class", className);

      $("#DialogWidgetContent").html(content);

      switch (className) {

      case "inlineStyle":

        if ("undefined" == typeof(width)) {

          width = "300"

        }

        if ("undefined" == typeof(height)) {

          height = "300"

        }

        scrolltopValue = $(positionTarget).offset().top;

        totalHeight = scrolltopValue + parseInt(height) + 
parseInt($("#DialogWidgetContainer").css("padding-top")) + 
parseInt($("#DialogWidgetContainer").css("padding-bottom"));

        if (totalHeight > $("body").height()) {

          scrolltopValue -= parseInt(height)

        }

        scrollleftValue = $(positionTarget).offset().left;

        totalWidth = scrollleftValue + parseInt(width) + 
parseInt($("#DialogWidgetContainer").css("padding-left")) + 
parseInt($("#DialogWidgetContainer").css("padding-right"));

        if (totalWidth > $("body").width()) {

          scrollleftValue -= parseInt(width)

        }

        break;

      default:

        if ("undefined" == typeof(width)) {

          width = "700"

        }

        if ($("body").scrollTop() > $("html").scrollTop()) {

          scrolltopValue = $("body").scrollTop()

        } else {

          scrolltopValue = $("html").scrollTop()

        }

      }

      dContainer.css("height", $("body").height());

      if ("undefined" != typeof(height)) {

        $("#DialogWidgetContent").css("height", height)

      }

      $("#DialogWidgetContainer, #DialogWidgetContent").css("width", width);

      if ("undefined" != typeof(scrolltopValue)) {

        $("#DialogWidgetContainer").css("top", scrolltopValue)

      }

      if ("undefined" != typeof(scrollleftValue)) {

        $("#DialogWidgetContainer").css("left", scrollleftValue)

      }

      $("body").addClass("displayDialog");

      if ("undefined" == typeof(height)) {

        if ($("body").scrollTop() > $("html").scrollTop()) {

          scrolltopValue = $("body").scrollTop()

        } else {

          scrolltopValue = $("html").scrollTop()

        }

        $("#DialogWidgetContainer").css("top", scrolltopValue + 25);

        heightDiff = CMApplication.Viewport.height - 
$("#DialogWidgetContainer").outerHeight();

        if (heightDiff < 0) {

          newHeight = $("#DialogWidgetContainer").height() - Math.abs(heightDiff) 
- 20;

          $("#DialogWidgetContainer").css("height", newHeight);

          $("#DialogWidgetContent").css("height", newHeight - 30);

          heightDiff = CMApplication.Viewport.height - 
$("#DialogWidgetContainer").outerHeight()

        }

      }

    }, close: function() {

      dContainer = CMApplication.Widgets.Dialog.dialogContainer;

      if (dContainer == null) {

        return

      }

      CMApplication.Widgets.Dialog.className = null;

      $("body").removeClass("displayDialog");

      $("#DialogWidget").attr("class", "");

      $("#DialogWidgetContent").html("");

      $("#DialogWidgetContainer").css("height", "auto");

      $("#DialogWidgetContent").css("height", "auto")

    }, _init: function() {

      markup = '<div id="DialogWidget"><div id="DialogWidgetBackground"></div><div 
id="DialogWidgetContainer"><div 
id="DialogWidgetClose"><span>close</span></div><div 
id="DialogWidgetContent"></div></div></div>';

      CMApplication.Widgets.Dialog.dialogContainer = $(markup).appendTo("body");

      dContainer = CMApplication.Widgets.Dialog.dialogContainer;

      $("#DialogWidgetBackground,#DialogWidgetClose").live("click", 
CMApplication.Widgets.Dialog.Events.close);

      $("#DialogWidgetContent form:not(.noDynamicSubmit 
form):not(#DialogWidgetContent #premiumPrices form)").live("submit", 
CMApplication.Widgets.Dialog.Events.submit)

    }

  };

  CMApplication.Widgets.AdvancedUpload = {

    _uploadServerHostname: null,

    getUploadServerHostname: function() {

      if (CMApplication.Widgets.AdvancedUpload._uploadServerHostname === null) {

        id = Math.floor(Math.random() * 50);

        CMApplication.Widgets.AdvancedUpload._uploadServerHostname = "s" + id + 
".wupload" + myTLD

      }

      return CMApplication.Widgets.AdvancedUpload._uploadServerHostname

    }, Uploads: {}, Progress: {

      updateResponse: function(uploadIdentifier, data) {

        CMApplication.Widgets.AdvancedUpload.setUploadProgress(uploadIdentifier, 
data)

      }

    }, Events: {

      close: function(e) {

        e.preventDefault();

        
CMApplication.Widgets.AdvancedUpload.close($(this).closest(".WebUploadWidget").att
r("rel"))

      }, minimize: function(e) {

        e.preventDefault();

        $("body").removeClass("displayWebUpload");

        uploadContainer = 
$("#WebUploadWidget").hide().addClass("uploadMinimized").attr("id", 
"WebUploadWidget_" + $("#WebUploadWidget").attr("rel"));

        minimizer = $("#WebUploadMinimizer");

        if (minimizer.length == 0) {

          xhtml = "";

          xhtml += '<div id="WebUploadMinimizer">';

          xhtml += "    <h3><span>" + CMApplication.Dictionnary.WEB_UPLOAD + 
"</span></h3>";

          xhtml += '    <ul class="actions">';

          xhtml += '        <li class="close"><a href="#"><span>' + 
CMApplication.Dictionnary.CLOSE + "</span></a></li>";

          xhtml += "    </ul>";

          xhtml += "</div>";

          minimizer = $(xhtml).appendTo($("body"));

          $("#WebUploadMinimizer").css("left", $("#container").offset().left)

        }

        xhtml = "";

        xhtml += '<div class="WebUploadWidget" rel="' + 
uploadContainer.attr("rel") + '">';

        if 
(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].files.length > 1) 
{

          heading = CMApplication.Dictionnary.UPLOADING + " " + 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].files.length + " " 
+ CMApplication.Dictionnary.FILES

        } else {

          heading = 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].files[0].name

        }

        xhtml += "    <h4><span>" + heading + "</span></h4>";

        xhtml += '    <ul class="actions">';

        xhtml += '        <li class="restore"><a href="#"><span>' + 
CMApplication.Dictionnary.RESTORE + "</span></a></li>";

        xhtml += '        <li class="close"><a href="#"><span>' + 
CMApplication.Dictionnary.CANCEL + "</span></a></li>";

        xhtml += "    </ul>";

        xhtml += "</div>";

        uploadMinimized = $(xhtml).appendTo(minimizer);

        uploadMinimized.attr("class", 
uploadContainer.attr("class")).removeClass("uploadMinimized");

        uploadMinimized.append($(".progressbar", uploadContainer).clone());

        uploadMinimized.append($(".WebUploadWidgetResult", 
uploadContainer).clone());

        window.location.href = "#mainContent";

        $("#mainContent").animate({

          paddingTop: minimizer.height() + 48

        })

      }, restore: function(e) {

        e.preventDefault();

        $("body").addClass("displayWebUpload");

        minimizerContainer = $(this).closest(".WebUploadWidget");

        uploadIdentifier = minimizerContainer.attr("rel");

        minimizerContainer.remove();

        if ($("#WebUploadMinimizer .WebUploadWidget").length == 0) {

          $("#WebUploadMinimizer").remove()

        }

        $('.WebUploadWidget[rel="' + uploadIdentifier + 
'"]').removeClass("uploadMinimized").attr("id", "WebUploadWidget").show();

        if ($("body").scrollTop() > $("html").scrollTop()) {

          scrolltopValue = $("body").scrollTop()

        } else {

          scrolltopValue = $("html").scrollTop()

        }

        $("#WebUploadWidget").css("top", scrolltopValue)

      }, submit: function(e) {

        uploadIdentifier = $("#WebUploadWidget").attr("rel");

        CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step = 
"progress";

        CMApplication.Widgets.AdvancedUpload.open(uploadIdentifier);

        if ("undefined" == (typeof 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].originalAction)) {

          
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].originalAction = 
$(this).attr("action")

        }

        $(this).attr("action", 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].originalAction + 
"?callbackUrl=" + CMApplication.URLs.domain + CMApplication.URLs.uploadCallback + 
"&X-Progress-ID=" + uploadIdentifier);

        $("body").prepend('<iframe class="webUploadProxy" name="' + 
uploadIdentifier + '" src="#"></iframe>');

        $(this).attr("target", uploadIdentifier);

        $('input[type="file"]', this).each(function(key, elem) {

          if ($(elem).val() == "") {

            $(elem).remove()

          }

        });

        
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload.lastUpdate = 
new Date().getTime();

        
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].progressTimer = 
setTimeout("CMApplication.Widgets.AdvancedUpload.getUploadProgress('" + 
uploadIdentifier + "');", 1000);

        $(".buttons", this).append('<button type="button" 
class="webUploadCancel"><span>' + CMApplication.Dictionnary.CANCEL_UPLOAD + 
"</span></button>");

        setTimeout("$('#WebUploadWidget button[type=\\"submit\\"]').remove();", 100)

      }, addFilesFromInstructionStep: function(event) {

        uploadIdentifier = $("#WebUploadWidget").attr("rel");

        CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step = 
"fileSelection";

        CMApplication.Widgets.AdvancedUpload.open(uploadIdentifier)

      }, addFiles: function(event) {

        CMApplication.Widgets.AdvancedUpload._updateFiles();

        $('<input type="file" name="files[]" multiple="multiple" 
/>').appendTo($("#WebUploadWidget form .files"))

      }

    }, start: function() {

      uploadIdentifier = "upload_" + new Date().getTime() + "_" + 
CMApplication.User.sessId + "_" + Math.floor(Math.random() * 90000);

      CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier] = {

        id: uploadIdentifier,

        files: [],

        step: "instructions",

        upload: {

          timerDelay: 1000,

          speed: 0,

          percent: 0,

          size: 0,

          lastSize: 0,

          total: 0

        }

      };

      eval("CMApplication.Widgets.AdvancedUpload.open" + 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step.charAt(0).toUp
perCase() + 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step.slice(1) + 
'("' + uploadIdentifier + '")')

    }, close: function(uploadIdentifier) {

      confirmation = true;

      uploadContainer = $('.uploadMinimized.WebUploadWidget[rel="' + 
uploadIdentifier + '"]');

      if (uploadContainer.is(".progress")) {

        confirmation = 
confirm(CMApplication.Dictionnary.LEAVING_WILL_CANCEL_UPLOADS)

      }

      if (confirmation) {

        $('iframe.webUploadProxy[name="' + uploadIdentifier + '"]').remove();

        $('.WebUploadWidget[rel="' + uploadIdentifier + '"]').remove();

        if ($("#WebUploadMinimizer .WebUploadWidget").length == 0) {

          $("#WebUploadMinimizer").remove()

        }

        if ($("#WebUploadWidget").length == 0) {

          $("body").removeClass("displayWebUpload")

        }

      }

    }, open: function(uploadIdentifier) {

      eval("CMApplication.Widgets.AdvancedUpload.open" + 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step.charAt(0).toUp
perCase() + 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step.slice(1) + 
'("' + uploadIdentifier + '")')

    }, _open: function(uploadIdentifier) {

      if ($("#WebUploadWidget").length > 0) {

        return

      }

      xhtml = "";

      xhtml += '<div id="WebUploadWidget" class="WebUploadWidget" rel="' + 
uploadIdentifier + '">';

      xhtml += '   <div class="WebUploadWidgetBackground"></div>';

      xhtml += '   <div class="WebUploadWidgetContainer">';

      xhtml += "       <h3><span>" + CMApplication.Dictionnary.WEB_UPLOAD + 
"</span></h3>";

      xhtml += '       <ul class="actions">';

      xhtml += '           <li class="restore"><a href=""><span>' + 
CMApplication.Dictionnary.RESTORE + "</span></a></li>";

      xhtml += '           <li class="minimize"><a href=""><span>' + 
CMApplication.Dictionnary.MINIMIZE + "</span></a></li>";

      xhtml += '           <li class="close"><a href=""><span>' + 
CMApplication.Dictionnary.CLOSE + "</span></a></li>";

      xhtml += "       </ul>";

      xhtml += '       <form action="http://' + 
CMApplication.Widgets.AdvancedUpload.getUploadServerHostname() + '" method="post" 
enctype="multipart/form-data">';

      if (jQuery.getCookie("email") != "") {

        xhtml += '           <div class="destination">';

        xhtml += '               <input type="hidden" name="folderId" 
class="destinationFolderId" value="0" />';

        xhtml += "           </div>"

      }

      xhtml += '           <div class="files">';

      xhtml += "               <label><span>" + 
CMApplication.Dictionnary.CHOOSE_FILES_TO_UPLOAD + "</span></label>";

      xhtml += '               <input type="file" name="files[]" 
multiple="multiple" />';

      xhtml += "           </div>";

      xhtml += '           <div class="buttons">';

      xhtml += '               <button type="submit" 
class="webUploadSubmit"><span>' + CMApplication.Dictionnary.START_UPLOAD + 
"</span></button>";

      xhtml += "           </div>";

      xhtml += "       </form>";

      xhtml += "   </div>";

      xhtml += "</div>";

      $("body").addClass("displayWebUpload").append(xhtml);

      if ($("body").scrollTop() > $("html").scrollTop()) {

        scrolltopValue = $("body").scrollTop()

      } else {

        scrolltopValue = $("html").scrollTop()

      }

      $("#WebUploadWidget").css("top", scrolltopValue)

    }, openComplete: function(uploadIdentifier, data) {

      CMApplication.Widgets.AdvancedUpload.setUploadProgress(uploadIdentifier, {

        total: 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload.total,

        current: 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload.total

      });

      
clearTimeout(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].progre
ssTimer);

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      
uploadContainer.addClass("complete").removeClass("instructions").removeClass("prog
ress").removeClass("fileSelection");

      var files = [];

      var failedCnt = 0;

      if (typeof data == "string") {

        
$(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].files).each(funct
ion(key, value) {

          failedCnt++;

          value.isSuccess = false;

          value.statusMessage = data;

          files.push(value)

        })

      } else {

        $(data).each(function(key, value) {

          file = {

            name: value.filename

          };

          switch (value.statusCode) {

          case 0:

            file.isSuccess = true;

            file.size = value.link.size;

            file.id = value.link.id;

            break;

          default:

            file.isSuccess = false;

            file.statusMessage = value.statusMessage;

            failedCnt++

          }

          files.push(file)

        })

      }

      CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].files = 
files;

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      if (uploadContainer.length > 0) {

        CMApplication.Widgets.AdvancedUpload._updateFiles(uploadIdentifier);

        $("form, .progressbar", uploadContainer).remove();

        if (failedCnt == 0) {

          resultClass = "success";

          resultHeading = CMApplication.Dictionnary.YOU_SUCCESSFULLY_UPLOADED + " 
" + files.length + " file" + (files.length > 1 ? "s" : "")

        } else {

          if (files.length > failedCnt) {

            resultClass = "warning";

            resultHeading = CMApplication.Dictionnary.YOU_UPLOADED + " " + 
(files.length - failedCnt) + " of " + files.length + 
CMApplication.Dictionnary.FILES

          } else {

            resultClass = "error";

            resultHeading = CMApplication.Dictionnary.ERROR_DURING_THE_UPLOAD

          }

        }

        xhtml = "";

        xhtml += '<div class="WebUploadWidgetResult ' + resultClass + '">';

        xhtml += "    <h4><span>" + resultHeading + "</span></h4>";

        xhtml += "</div>";

        if (files.length != failedCnt) {

          xhtml += '    <a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", "") + '" 
class="viewAllLinks"><span>' + CMApplication.Dictionnary.SHARE_FILES + 
"</span></a>"

        }

        uploadContainer.each(function(key, container) {

          if ($(container).parent().is("body")) {

            $(".WebUploadWidgetContainer", container).append(xhtml)

          } else {

            $(container).append(xhtml)

          }

        })

      }

      if ($("#fileBrowser").length == 1) {

        CMApplication.Widgets.FileManager.FileBrowser.browse()

      }

      $('iframe.webUploadProxy[name="' + uploadIdentifier + '"]').remove()

    }, openInstructions: function(uploadIdentifier) {

      CMApplication.Widgets.AdvancedUpload._open(uploadIdentifier);

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      
uploadContainer.addClass("instructions").removeClass("complete").removeClass("file
Selection").removeClass("progress");

      if ($("div.instructions", uploadContainer).length == 0) {

        xhtml = "";

        xhtml += '       <div class="instructions">';

        xhtml += "           <p>" + 
CMApplication.Dictionnary.CHOOSE_FILES_AND_THEN_PRESS_UPLOAD_NOW + "</p>";

        xhtml += "       </div>";

        $(xhtml).insertAfter($("ul.actions", uploadContainer))

      }

    }, openFileSelection: function(uploadIdentifier) {

      CMApplication.Widgets.AdvancedUpload._open(uploadIdentifier);

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      
uploadContainer.addClass("fileSelection").removeClass("complete").removeClass("ins
tructions").removeClass("progress");

      $(".files label span", uploadContainer).text("Add More Files");

      if ($("table", uploadContainer).length == 0) {

        xhtml = "";

        xhtml += '       <div class="fileListing">';

        xhtml += "       <table>";

        xhtml += "           <thead>";

        xhtml += "               <tr>";

        xhtml += '                   <th class="fileName" colspan="2">' + 
CMApplication.Dictionnary.FILE_NAME + "</th>";

        xhtml += "               </tr>";

        xhtml += "           </thead>";

        xhtml += "           <tbody>";

        xhtml += "           </tbody>";

        xhtml += "       </table>";

        xhtml += "       </div>";

        $(xhtml).insertBefore($("form", uploadContainer))

      }

    }, openProgress: function(uploadIdentifier) {

      CMApplication.Widgets.AdvancedUpload._open(uploadIdentifier);

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      
uploadContainer.addClass("progress").removeClass("complete").removeClass("instruct
ions").removeClass("fileSelection");

      if ($("div.progressbar", uploadContainer).length == 0) {

        xhtml = "";

        xhtml += '       <div class="progressbar">';

        xhtml += "           <strong>" + CMApplication.Dictionnary.PLEASE_WAIT + 
"</strong>";

        xhtml += '           <div class="total">';

        xhtml += '              <div class="progress">';

        xhtml += "              </div>";

        xhtml += "           </div>";

        xhtml += '           <div class="info">';

        xhtml += '               <span class="percent">0%</span>';

        xhtml += '               <span class="speed">0b/s</span>';

        xhtml += "           </div>";

        xhtml += "       </div>";

        $(xhtml).insertAfter($("form", uploadContainer));

        CMApplication.Widgets.AdvancedUpload.updateProgress(uploadIdentifier, 500)

      }

    }, updateProgress: function(uploadIdentifier, nextCallDelay) {

      uploadContainers = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      uploadContainers.each(function(key, value) {

        uploadContainer = $(value);

        if ($("div.progressbar", uploadContainer).length > 0) {

          myUpload = 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload;

          $("div.progressbar span.percent", uploadContainer).text(myUpload.percent 
+ "%");

          $("div.progressbar span.speed", 
uploadContainer).text(CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.getHu
manReadableSize(myUpload.speed) + "/s");

          newWidth = "" + Math.round(myUpload.percent) + "%";

          $(".progress", uploadContainer).css("width", newWidth)

        }

      })

    }, getUploadProgress: function(uploadIdentifier) {

      if 
(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload.percent < 
100) {

        jQuery.ajax({

          url: "/keep-alive.php",

          cache: false,

          global: false

        });

        xhtml = '<script type="text/javascript" src="' + 
CMApplication.URLs.uploadProgress.replace(":unique", new 
Date().getTime().toString()).replace(":hostserver", 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].originalAction).rep
lace(":progress_key", uploadIdentifier).replace(":progress_key", uploadIdentifier) 
+ '"><\\/script>';

        $("body").append(xhtml)

      }

    }, setUploadProgress: function(uploadIdentifier, data) {

      if ("undefined" == (typeof 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier])) {

        return

      }

      uploadStatus = 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload;

      now = new Date().getTime();

      uploadStatus.lastSize = uploadStatus.size;

      uploadStatus.size = data.current;

      uploadStatus.total = data.total;

      uploadStatus.percent = Math.round(data.current * 100 / data.total);

      if (uploadStatus.percent >= 100) {

        
clearTimeout(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].progre
ssTimer);

        uploadStatus.percent = 100

      }

      if ("undefined" == (typeof uploadStatus.onePercentSize)) {

        uploadStatus.onePercentSize = 1 / 100 * data.total

      }

      if (uploadStatus.lastUpdate != now) {

        uploadStatus.speed = (uploadStatus.size - uploadStatus.lastSize) / 
((parseInt(now) - parseInt(uploadStatus.lastUpdate)) / 1000)

      } else {

        uploadStatus.speed = 0

      }

      timerDelay = 0;

      if (uploadStatus.percent < 100) {

        nextSizeProgressCall = (uploadStatus.percent + 1) * 
uploadStatus.onePercentSize;

        byteDiff = nextSizeProgressCall - uploadStatus.size;

        timerDelay = Math.ceil(byteDiff / uploadStatus.speed * 1000);

        if (timerDelay < 500) {

          timerDelay = 300

        }

        if (timerDelay > 8000) {

          timerDelay = 8000

        }

        
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].progressTimer = 
setTimeout("CMApplication.Widgets.AdvancedUpload.getUploadProgress('" + 
uploadIdentifier + "')", timerDelay)

      }

      uploadStatus.lastUpdate = now;

      CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload = 
uploadStatus;

      CMApplication.Widgets.AdvancedUpload.updateProgress(uploadIdentifier, 
timerDelay)

    }, _updateFiles: function(uploadIdentifier) {

      if ("undefined" == (typeof uploadIdentifier) && $("#WebUploadWidget").length 
> 0) {

        uploadIdentifier = $("#WebUploadWidget").attr("rel")

      }

      if ("undefined" == (typeof uploadIdentifier)) {

        return

      }

      uploadContainer = $('.WebUploadWidget[rel="' + uploadIdentifier + '"]');

      filesElements = $('form input[type="file"]', uploadContainer);

      if (filesElements.length > 0 && 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step != "complete") 
{

        var files = [];

        $(filesElements).each(function(key, input) {

          if ("undefined" != (typeof input.files)) {

            $(input.files).each(function(key, value) {

              files.push({

                name: value.name,

                size: value.size

              })

            })

          } else {

            files.push({

              name: $(input).val(),

              size: null

            })

          }

        });

        CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier]["files"] = 
files

      }

      var xhtml = "";

      var totalSize = 0;

      
$(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier]["files"]).each(fu
nction(key, file) {

        trClass = new Array();

        if (CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step == 
"complete") {

          trClass.push(file.isSuccess ? "success" : "fail")

        }

        if (! (key % 2)) {

          trClass.push("odd")

        }

        xhtml += "               <tr" + (trClass.length > 0 ? ' class="' + 
trClass.join(" ") + '"' : "") + 
(CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step == "complete" 
&& file.isSuccess ? ' rel="F' + file.id + '"' : "") + ">";

        colspan = 2;

        addxhtml = "";

        if (CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].step == 
"complete") {

          if (!file.isSuccess) {

            colspan = 1;

            addxhtml += '                   <th class="message"><strong>' + 
CMApplication.Dictionnary.FAIL + "</strong> " + file.statusMessage + "</th>"

          }

        }

        xhtml += '                   <th class="fileName" colspan="' + colspan + 
'"><span>' + file.name + "</span></th>";

        xhtml += addxhtml;

        xhtml += "               </tr>"

      });

      $("table tbody", uploadContainer).html(xhtml);

      CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier].upload.total 
= totalSize

    }, _init: function() {

      $("#div_adv_upload_files .chooseFiles a").live("click", function(e) {

        e.preventDefault();

        CMApplication.Widgets.AdvancedUpload.start()

      });

      $(".WebUploadWidget li.restore a").live("click", 
CMApplication.Widgets.AdvancedUpload.Events.restore);

      $("#WebUploadMinimizer > ul.actions li.close a").live("click", function(e) {

        e.preventDefault();

        $("#WebUploadMinimizer .WebUploadWidget li.close a").trigger("click")

      });

      $(".WebUploadWidget li.close a, .WebUploadWidget 
.webUploadCancel").live("click", 
CMApplication.Widgets.AdvancedUpload.Events.close);

      $(".WebUploadWidget li.minimize a").live("click", 
CMApplication.Widgets.AdvancedUpload.Events.minimize);

      $(".WebUploadWidget.fileSelection form").live("submit", 
CMApplication.Widgets.AdvancedUpload.Events.submit);

      if (jQuery.browser.msie) {

        $('.WebUploadWidget.instructions input[type="file"]').live("click", 
function(e) {

          $("#inputFileSelection").removeAttr("id");

          clearTimeout(ieFixForFileSelectionOnChangeEventTimer);

          $(this).attr("id", "inputFileSelection");

          ieFixForFileSelectionOnChangeEventTimer = 
setTimeout("ieFixForFileSelectionOnChangeEvent()", 200)

        })

      }

      $('.WebUploadWidget.instructions input[type="file"]').live("change", 
CMApplication.Widgets.AdvancedUpload.Events.addFilesFromInstructionStep);

      $('.WebUploadWidget input[type="file"]').live("change", 
CMApplication.Widgets.AdvancedUpload.Events.addFiles);

      $(".WebUploadWidget tbody td.share a").live("click", function(e) {

        e.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"))

      });

      $(".WebUploadWidget tbody td.link a").live("click", function(e) {

        e.preventDefault();

        $(this).closest("tr").next().toggle()

      });

      $(".WebUploadWidget tfoot td.link a").live("click", function(e) {

        e.preventDefault();

        $(".WebUploadWidgetContainer a.viewAllLinks", 
$(this).closest(".WebUploadWidget")).trigger("click")

      });

      $(".WebUploadWidgetContainer a.viewAllLinks").live("click", function(e) {

        e.preventDefault();

        var ids = new Array();

        $('.WebUploadWidget[rel="' + 
$(this).closest(".WebUploadWidget").attr("rel") + '"] table tbody 
tr.success:not(.links)').each(function(key, value) {

          ids.push($(value).attr("rel"))

        });

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("href") + ids)

      })

    }

  };

  CMApplication.Widgets.Upload = {

    Events: {

      submit: function(event) {

        uploadIdentifier = "upload_" + new Date().getTime() + "_" + 
CMApplication.User.sessId + "_" + Math.floor(Math.random() * 90000);

        if (undefined != $("#input-file")[0] && undefined != $("#input-
file")[0].files && undefined != $("#input-file")[0].files.length && $("#input-
file")[0].files.length > 1) {

          uploadFilename = "Upload of " + $("#input-file")[0].files.length + " 
files"

        } else {

          uploadFilename = $('input[type="file"]', this).val()

        }

        if (!$("form.webUpload").attr("originalAction")) {

          $("form.webUpload").attr("originalAction", 
$("form.webUpload").attr("action"))

        }

        $("form.webUpload").attr("action", 
$("form.webUpload").attr("originalAction") + "/?X-Progress-ID=" + 
uploadIdentifier);

        $("body").prepend('<iframe rel="' + uploadIdentifier + '" 
originalAction="' + $("form.webUpload").attr("originalAction") + '" class="upload" 
name="' + uploadIdentifier + '" src="#"></iframe>');

        $(this).attr("target", uploadIdentifier);

        CMApplication.Widgets.Upload.Progress._construct(uploadIdentifier, 
uploadFilename);

        setTimeout("if ($('.webUpload').length > 0) $('.webUpload')[0].reset()", 
500);

        callbackUrlField = $('input[name="callbackUrl"]', this);

        if (callbackUrlField.length == 0) {

          callbackUrlField = jQuery('<input type="hidden" name="callbackUrl" 
value="" />').appendTo($(this))

        }

        callbackUrlField.val(CMApplication.URLs.domain + 
CMApplication.URLs.uploadCallback);

        if (CMApplication.User.role == CMApplication.User.RolesValues.ANONYMOUS) {

          $("#quickUpload").hide()

        }

        if (false && $("iframe.upload").length == 1) {

          CMApplication.Widgets.Ajax.start()

        }

      }

    }, Progress: {

      InProgressTimer: {}, _construct: function(uploadIdentifier, uploadFilename) 
{

        uploadStatusWrapper = $("#uploadStatusWrapper");

        if (uploadStatusWrapper.length == 0) {

          $('<div id="uploadStatusContainer"><h3>' + 
CMApplication.Dictionnary.YOUR_UPLOADS + '</h3><div 
id="uploadStatusWrapper"></div><a id="viewAllLinks" href="">' + 
CMApplication.Dictionnary.VIEW_ALL_LINKS + "</a></div>").appendTo("body");

          $("#viewAllLinks").live("click", function(event) {

            event.preventDefault();

            var patt1 = new RegExp("[^/]*$");

            var links = "";

            $("#uploadStatusWrapper a.link").each(function() {

              links += patt1.exec($(this).attr("href")) + ","

            });

            
CMApplication.Widgets.Dialog.displayUrl(CMApplication.URLs.languageFilesystemGener
ateLink.replace(":id", links))

          });

          uploadStatusWrapper = $("#uploadStatusWrapper")

        }

        if (uploadFilename.length > 37) {

          uploadFilename = uploadFilename.substring(0, 17) + "..." + 
uploadFilename.substring(uploadFilename.length - 17)

        }

        uploadStatusWrapper.append('<div id="' + uploadIdentifier + '" 
class="uploadStatus"><span class="filename">' + uploadFilename + '</span><div 
class="progressBar"><div class="state"></div></div><span 
class="percentageCompleted"></span></div>');

        CMApplication.Widgets.Upload.Progress.updateRequest(uploadIdentifier)

      }, complete: function(uploadIdentifier, results) {

        
clearTimeout(CMApplication.Widgets.Upload.Progress.InProgressTimer[uploadIdentifie
r]);

        $("#" + uploadIdentifier + " .progressBar").remove();

        $('iframe[rel="' + uploadIdentifier + '"]').remove();

        var xhtml = "";

        var errorsMsg = "";

        var successLinks = [];

        $(results).each(function(key, value) {

          xhtml += '<div class="element">';

          if (value.statusCode == 0 && value.linkId != 0) {

            successLinks.push(value.linkId)

          } else {

            xhtml += CMApplication.Dictionnary.ERROR + " <span>" + value.filename 
+ "</span>";

            errorsMsg += "<li><strong>" + value.filename + "</strong>: " + 
value.statusMessage + "</li>"

          }

          xhtml += "</div>"

        });

        if (successLinks.length > 0) {

          viewLinkUrl = 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", 
successLinks.join(","));

          xhtml += '<div class="element">';

          xhtml += CMApplication.Dictionnary.COMPLETED + " ";

          xhtml += '<a href="' + viewLinkUrl + '" 
onclick="CMApplication.Widgets.Dialog.displayUrl(this.href, 700); return false;" 
class="link" title="' + CMApplication.Dictionnary.VIEW_LINKS + '"><span>' + 
CMApplication.Dictionnary.VIEW_LINKS + "</span></a>";

          xhtml += "</div>"

        }

        xhtml += '<a href="#" 
onclick="CMApplication.Widgets.Upload.Progress.close(\\'' + uploadIdentifier + 
'\\'); return false;" class="close" title="' + CMApplication.Dictionnary.CLOSE + 
'"><span>' + CMApplication.Dictionnary.CLOSE + "</span></a>";

        $("#" + uploadIdentifier + " .percentageCompleted").html(xhtml);

        if (false && $("iframe.upload").length == 0) {

          CMApplication.Widgets.Ajax.stop()

        }

        if (errorsMsg != "") {

          errorsMsg = CMApplication.Dictionnary.FOLLOWING_ERROR_DURING_UPLOAD + 
"<ul>" + errorsMsg + "</ul>";

          CMApplication.Widgets.Dialog.displayMessage(errorsMsg, 
CMApplication.Widgets.Dialog.Types.error)

        }

      }, close: function(uploadIdentifier) {

        $("#" + uploadIdentifier).remove();

        if ($("#uploadStatusWrapper").children().length == 0) {

          $("#uploadStatusContainer").remove()

        }

      }, updateRequest: function(uploadIdentifier) {

        jQuery.ajax({

          url: "/keep-alive.php",

          cache: false

        });

        xhtml = '<script type="text/javascript" src="' + 
CMApplication.URLs.uploadProgress.replace(":unique", new 
Date().getTime().toString()).replace(":hostserver", $('iframe[rel="' + 
uploadIdentifier + '"]').attr("originalAction")).replace(":progress_key", 
uploadIdentifier).replace(":progress_key", uploadIdentifier) + '"></script>';

        CMApplication.Widgets.Upload.Progress.InProgressTimer[uploadIdentifier] = 
setTimeout("$('body').append('" + xhtml + "');", 2000)

      }, updateResponse: function(uploadIdentifier, data) {

        if ("undefined" != (typeof 
CMApplication.Widgets.AdvancedUpload.Uploads[uploadIdentifier])) {

          CMApplication.Widgets.AdvancedUpload.setUploadProgress(uploadIdentifier, 
data)

        } else {

          if (data.current != null) {

            percent = Math.ceil(parseInt(data.current) / parseInt(data.total) * 
100).toString() + "%";

            $("#" + uploadIdentifier + " .state").css("width", percent);

            if (data.percent != 100) {

              
CMApplication.Widgets.Upload.Progress.updateRequest(uploadIdentifier);

              $("#" + uploadIdentifier + " .percentageCompleted").text(percent)

            }

          }

        }

      }

    }, _init: function() {

      $(".webUpload").live("submit", CMApplication.Widgets.Upload.Events.submit)

    }

  };

  CMApplication.Widgets.Internationalization = {

    widgetLink: $("#internationalization"),

    Events: {

      open: function(e) {

        if (!$(this).hasClass("active")) {

          e.preventDefault();

          e.stopPropagation();

          CMApplication.Widgets.Internationalization.open(this)

        }

      }, close: function(e) {

        CMApplication.Widgets.Internationalization.close()

      }

    }, open: function() {

      this.widgetLink.addClass("active");

      $(document).bind("click", this.Events.close)

    }, close: function() {

      this.widgetLink.removeClass("active");

      $(document).unbind("click", this.Events.close)

    }

  };

  CMApplication.Widgets.FolderBrowser = {

    url: CMApplication.URLs.languageFilesystemBrowse.replace[a-z]*/gi, "") + 
"?partial=folderTree&widget=folderBrowser&orderFoldersBy=name&orderFoldersDirectio
n=desc",

    response: null,

    browse: function(folderId) {

      $("#selectAllFiles").attr("checked", null);

      $("#globalSearch").attr("checked", null);

      if (folderId == undefined) {

        var myUrl = CMApplication.Widgets.FolderBrowser.url

      } else {

        var myUrl = CMApplication.Widgets.FolderBrowser.url.replace("list?", 
"list/" + folderId + "?")

      }

      $.ajax({

        async: false,

        url: myUrl,

        dataType: "html",

        success: function(data, textStatus, XMLHttpRequest) {

          CMApplication.Widgets.FolderBrowser.response = data

        }

      });

      list = "<ul>" + CMApplication.Widgets.FolderBrowser.response + "</ul>";

      return list

    }

  };

  CMApplication.Widgets.FileManager = {

    Items: {

      _items: {}, add: function(items) {

        CMApplication.Widgets.FileManager.Items._items = jQuery.extend({}, 
CMApplication.Widgets.FileManager.Items._items, items)

      }, getInfo: function(id) {

        return CMApplication.Widgets.FileManager.Items._items[id]

      }

    }, History: {

      log: [0],

      current: 0,

      addLog: function(folderId) {

        CMApplication.Widgets.FileManager.History.log.push(folderId)

      }

    }, NavigationBar: {

      Parent: {

        linkElement: $("#navigationBar li.parent a"),

        Events: {

          click: function(event) {

            event.preventDefault();

            parentFolder = $("#folderTree li:has(li.active)");

            if (parentFolder.length == 0) {

              return

            }

            folderId = parentFolder.attr("rel");

            CMApplication.Widgets.FileManager.FileBrowser.browse(folderId);

            
CMApplication.Widgets.FileManager.NavigationBar.Parent.updateLinkStyle()

          }

        }, updateLinkStyle: function() {

          parentFolder = $("#folderTree li:has(li.active)");

          linkElement = 
CMApplication.Widgets.FileManager.NavigationBar.Parent.linkElement;

          if (parentFolder.length == 0) {

            linkElement.addClass("disabled")

          } else {

            linkElement.removeClass("disabled")

          }

        }

      }, New: {

        linkElement: $("#navigationBar li.new a"),

        Events: {

          click: function(event) {

            event.preventDefault();

            currentFolderId = $("#folderTree li.active").attr("rel");

            
CMApplication.Widgets.FileManager.FileBrowser.newFolder(currentFolderId)

          }

        }

      }, GenerateLink: {

        linkElement: $("#navigationBar li.links a"),

        Events: {

          submit: function(event) {

            event.preventDefault();

            event.stopPropagation();

            var myUrl = $(this).attr("action");

            var myParams = $(this).serialize();

            jQuery.ajax({

              async: false,

              url: myUrl,

              type: "POST",

              data: myParams,

              dataType: "html",

              success: function(data, textStatus, XMLHttpRequest) {

                CMApplication.Widgets.Dialog.displayContent(data);

                
$("#linksForm").submit(CMApplication.Widgets.FileManager.NavigationBar.GenerateLin
k.Events.submit)

              }

            })

          }, click: function(event) {

            event.preventDefault();

            elementsId = [];

            $("#fileList li.selected").each(function() {

              elementsId.push($(this).attr("rel"))

            });

            if (elementsId.length == 0) {

              
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_G
ENERATELINKS_INSTRUCTION, CMApplication.Widgets.Dialog.Types.notice);

              return

            }

            var xHtml = "";

            jQuery.ajax({

              async: false,

              url: 
CMApplication.URLs.languageFilesystemGenerateLink.replace("/:id", ""),

              type: "POST",

              data: {

                id: elementsId.join(",")

              }, dataType: "html",

              success: function(data, textStatus, XMLHttpRequest) {

                xHtml = data

              }

            });

            CMApplication.Widgets.Dialog.displayContent(xHtml);

            
$("#linksForm").submit(CMApplication.Widgets.FileManager.NavigationBar.GenerateLin
k.Events.submit)

          }

        }

      }, Premium: {

        linkElement: $("#navigationBar li.premium a"),

        Events: {

          click: function(event) {

            if (!$("#selectAllFolder").attr("checked")) {

              event.preventDefault();

              elementsId = [];

              $("#fileList li.selected").each(function() {

                elementsId.push($(this).attr("rel"))

              });

              if (elementsId.length == 0) {

                
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_P
REMIUM_INSTRUCTION, CMApplication.Widgets.Dialog.Types.notice);

                return

              }

            } else {

              elementsId = [-1]

            }

            CMApplication.Widgets.FileManager.FileBrowser.premium(elementsId)

          }

        }, updateLinkStyle: function() {

          parentFolder = $("#folderTree li:has(li.active)");

          linkElement = 
CMApplication.Widgets.FileManager.NavigationBar.Premium.linkElement;

          if ($("#fileList li.selected").length == 0) {

            linkElement.addClass("disabled")

          } else {

            linkElement.removeClass("disabled")

          }

        }

      }, Unpremium: {

        linkElement: $("#navigationBar li.unsetPremium a"),

        Events: {

          click: function(event) {

            event.preventDefault();

            elementsId = [];

            $("#fileList li.selected").each(function() {

              elementsId.push($(this).attr("rel"))

            });

            if (elementsId.length == 0) {

              
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_P
REMIUM_INSTRUCTION, CMApplication.Widgets.Dialog.Types.notice);

              return

            }

            CMApplication.Widgets.FileManager.FileBrowser.unpremium(elementsId)

          }

        }, updateLinkStyle: function() {

          parentFolder = $("#folderTree li:has(li.active)");

          linkElement = 
CMApplication.Widgets.FileManager.NavigationBar.Unpremium.linkElement;

          if ($("#fileList li.selected").length == 0) {

            linkElement.addClass("disabled")

          } else {

            linkElement.removeClass("disabled")

          }

        }

      }, Upload: {

        linkElement: $('#navigationBar li.upload a[href="#"]'),

        Events: {

          click: function(event) {

            event.preventDefault();

            CMApplication.Widgets.AdvancedUpload.start();

            $("#WebUploadWidget .destinationFolderId").val($("#folderTree 
li.active").attr("rel").replace("D", ""))

          }

        }

      }, updateLinksStyles: function() {

        CMApplication.Widgets.FileManager.NavigationBar.Parent.updateLinkStyle();

        CMApplication.Widgets.FileManager.NavigationBar.Premium.updateLinkStyle();

        
CMApplication.Widgets.FileManager.NavigationBar.Unpremium.updateLinkStyle();

        $("#selectAllFiles").attr("checked", null)

      }, _init: function() {

        CMApplication.Widgets.FileManager.NavigationBar.updateLinksStyles();

        
CMApplication.Widgets.FileManager.NavigationBar.Parent.linkElement.bind("click", 
CMApplication.Widgets.FileManager.NavigationBar.Parent.Events.click);

        
CMApplication.Widgets.FileManager.NavigationBar.New.linkElement.bind("click", 
CMApplication.Widgets.FileManager.NavigationBar.New.Events.click);

        
CMApplication.Widgets.FileManager.NavigationBar.Upload.linkElement.bind("click", 
CMApplication.Widgets.FileManager.NavigationBar.Upload.Events.click);

        
CMApplication.Widgets.FileManager.NavigationBar.Premium.linkElement.bind("click", 
CMApplication.Widgets.FileManager.NavigationBar.Premium.Events.click);

        
CMApplication.Widgets.FileManager.NavigationBar.Unpremium.linkElement.bind("click"
, CMApplication.Widgets.FileManager.NavigationBar.Unpremium.Events.click);

        
CMApplication.Widgets.FileManager.NavigationBar.GenerateLink.linkElement.bind("cli
ck", CMApplication.Widgets.FileManager.NavigationBar.GenerateLink.Events.click)

      }

    }, NavigationHelper: {

      selectAll: {

        selectAll: function() {

          if ($("input.select:not(:checked)").length) {

            $("div.selectAll > input").attr("checked", true);

            $("input.select:not(:checked)").attr("checked", 
true).parent("li").addClass("selected")

          } else {

            $("div.selectAll > input").attr("checked", false);

            $("input.select:checked").attr("checked", 
false).parent("li").removeClass("selected")

          }

          CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update();

          CMApplication.Widgets.FileManager.NavigationBar.updateLinksStyles()

        }

      }, selectAllFolder: {

        selectAllFolder: function() {

          CMApplication.Widgets.FileManager.NavigationBar.updateLinksStyles()

        }

      }, sortBy: {

        update: function() {

          box = $("#sortForm");

          type = $("select", box).val();

          switch (type) {

          case "folder":

            $("li.size, li.downloads, li.sales", box).addClass("disabled");

            break;

          default:

            $("li.size, li.downloads, li.sales", box).removeClass("disabled")

          }

          $("li.asc, li.desc", box).removeClass("asc").removeClass("desc");

          $("li." + $('input[name="' + type + '_field"]', box).val(), 
box).addClass($('input[name="' + type + '_direction"]', box).val())

        }, sortBy: function() {

          $("#selectAllFiles").attr("checked", null);

          if 
(window.location.href.indexOf(CMApplication.URLs.languageFilesystemRemoved) > -1) 
{

            CMApplication.foward(CMApplication.URLs.languageFilesystemRemoved + 
"/1/" + $('#sortForm input[name="file_field"],#sortby').val() + "/" + $('#sortForm 
input[name="file_direction"],#direction').val())

          } else {

            type = $("#sortForm select").val();

            if (type == "folder") {

              var mylist = $("#ul_dirs");

              var listitems = mylist.children("li").get();

              listitems.sort(sortFolders);

              $.each(listitems, function(idx, itm) {

                mylist.append(itm)

              });

              ullist = $("#folderTree li. ul").get();

              $.each(ullist, function(idx0, itm0) {

                listitems = $(itm0).children("li").get();

                listitems.sort(sortFolders);

                $.each(listitems, function(idx, itm) {

                  $(itm0).append(itm)

                })

              })

            } else {

              CMApplication.Widgets.FileManager.FileBrowser.browse(undefined, 
false)

            }

          }

        }

      }, setDisplayLinks: {

        setDisplayLinks: function() {

          $.post("/file-manager/set-link-count", {

            linkCount: $("#linksToDisplay").val()

          }, function(data) {

            CMApplication.Widgets.FileManager.FileBrowser.browse()

          })

        }

      }, _init: function() {

        $("div.selectAll a").live("click", function(event) {

          event.preventDefault();

          CMApplication.Widgets.FileManager.NavigationHelper.selectAll.selectAll()

        });

        $("div.selectAll input").live("click", function(event) {

          CMApplication.Widgets.FileManager.NavigationHelper.selectAll.selectAll()

        });

        $("#selectAllFolder").live("click", function(event) {

          
CMApplication.Widgets.FileManager.NavigationHelper.selectAllFolder.selectAllFolder
()

        });

        $("#linksToDisplay").live("change", function(event) {

          $("#selectAllFiles").attr("checked", null);

          
CMApplication.Widgets.FileManager.NavigationHelper.setDisplayLinks.setDisplayLinks
()

        });

        $("#searchForm").submit(function(event) {

          event.preventDefault();

          $(".paginator b").replaceWith($(".paginator b big a"));

          $(".paginator > a:nth-child(2)").wrap("<b><big /></b>");

          $("#selectAllFiles").attr("checked", false);

          isSearchResult = $("#queryString").val();

          if ($("#globalSearch").attr("checked")) {

            isGlobalSearch = 1

          }

          CMApplication.Widgets.FileManager.FileBrowser.browse()

        });

        $("#sortForm").submit(function(event) {

          event.preventDefault();

          CMApplication.Widgets.FileManager.NavigationHelper.sortBy.sortBy()

        });

        $("#sortForm li:not(.disabled) a").click(function(event) {

          event.preventDefault();

          container = $("#sortForm");

          isAsc = $(this).parent().hasClass("asc");

          direction = isAsc ? "desc" : "asc";

          $("li.asc, li.desc", container).removeClass("asc").removeClass("desc");

          $(this).parent().addClass(direction);

          field = $(this).parent().attr("class").replace("asc", 
"").replace("desc", "").replace(" ", "");

          type = $("select", container).val();

          $('#sortForm input[name="' + type + '_field"]').val(field);

          $('#sortForm input[name="' + type + '_direction"]').val(direction);

          CMApplication.Widgets.FileManager.NavigationHelper.sortBy.sortBy()

        });

        $("#sortForm select").change(function(event) {

          event.preventDefault();

          
setTimeout("CMApplication.Widgets.FileManager.NavigationHelper.sortBy.update()", 
200)

        })

      }

    }, FileBrowser: {

      browserElement: $("#fileBrowser"),

      Events: {

        browse: function(event) {

          if ($(this).closest("li").attr("rel") == "D0") {

            isGlobalSearch = 1;

            $("#globalSearch").attr("checked", true);

            $("#queryStringLabel 
span").text(CMApplication.Dictionnary.SEARCH_ALL_FOLDERS)

          } else {

            isGlobalSearch = 0;

            $("#globalSearch").attr("checked", false);

            $("#queryStringLabel 
span").text(CMApplication.Dictionnary.SEARCH_THIS_FOLDERS)

          }

          event.stopPropagation();

          event.preventDefault();

          isSearchResult = false;

          $("#queryString").val("");

          $("#selectAllFiles").attr("checked", false);

          if ($(this).closest("li").hasClass("collapse")) {

            $(this).closest("li").trigger("click")

          }

          
CMApplication.Widgets.FileManager.FileBrowser.browse($(this).closest("li").attr("r
el"))

        }, search: function(event) {

          event.stopPropagation();

          event.preventDefault();

          
CMApplication.Widgets.FileManager.FileBrowser.browse($(this).closest("li").attr("r
el"))

        }

      }, getUrl: function(folderId) {

        if (folderId === undefined) {

          folderId = $("#folderTree li.active").length == 1 ? $("#folderTree 
li.active").attr("rel") : "D0"

        }

        queryString = $("#queryString").val();

        globalSearch = $("#globalSearch:checked").val() == 1 ? 1 : 0;

        orderBy = $('#sortForm input[name="file_field"]').val();

        orderDirection = $('#sortForm input[name="file_direction"]').val();

        page = $('.paginator input[name="page"]').length == 1 ? 
parseInt($('.paginator input[name="page"]').val()) : 1;

        myUrl = CMApplication.URLs.languageFilesystemBrowse;

        myUrl = myUrl.replace(":folderId", urlencode(folderId));

        myUrl = myUrl.replace(":page", urlencode(page));

        myUrl = myUrl.replace(":orderBy", urlencode(orderBy));

        myUrl = myUrl.replace(":orderDirection", urlencode(orderDirection));

        myUrl = myUrl.replace(":globalSearch", urlencode(globalSearch));

        myUrl = myUrl.replace(":queryString", urlencode(queryString));

        return myUrl

      }, browse: function(folderId, addLog) {

        $("#selectAllFiles").attr("checked", false);

        var addLog;

        if (typeof(addLog) !== "boolean") {

          addLog = true

        }

        if (folderId === undefined) {

          folderId = $("#folderTree li.active").length == 1 ? $("#folderTree 
li.active").attr("rel") : "D0"

        }

        jQuery.ajax({

          url: CMApplication.Widgets.FileManager.FileBrowser.getUrl(folderId) + 
"?partial=fileList",

          type: "POST",

          data: {

            folderId: folderId

          }, dataType: "html",

          success: function(data, textStatus, XMLHttpRequest) {

            queryParams = jQuery.unparam(this.data);

            folderId = queryParams.folderId;

            CMApplication.Widgets.FileManager.FileBrowser.FileList.populate(data, 
folderId);

            
CMApplication.Widgets.FileManager.FileBrowser.FolderTree.updateActiveElement(folde
rId);

            if (addLog) {

              CMApplication.Widgets.FileManager.History.addLog(folderId)

            }

            CMApplication.Widgets.FileManager.NavigationBar.updateLinksStyles();

            CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update()

          }

        })

      }, move: function(filesId) {

        if ($("#selectAllFiles").attr("checked")) {

          if (typeof(totalItemCount) == "undefined") {

            totalItemCount = totalFilesInFolder

          }

          if (totalItemCount > 100) {

            if (!confirm("Are you sure you want to move " + totalItemCount + " 
files?")) {

              return

            }

          }

        }

        if ($("#folderTree li.root > ul").length == 1) {

          $("#folderTree li.root ul script").remove();

          list = "<ul>" + $("#folderTree li.root > ul").html() + "</ul>"

        } else {

          list = CMApplication.Widgets.FolderBrowser.browse()

        }

        html = "<h4>" + CMApplication.Dictionnary.SELECT_A_DESTINATION + "</h4>";

        var action = CMApplication.URLs.languageFilesystemMove;

        html += '<form id="selectMoveDestinationForm" action="' + action + '"><div 
class="content folderTree" id="selectMoveDestination">';

        html += '   <input type="hidden" name="destination" value="" />';

        if (!$("#selectAllFiles").attr("checked")) {

          for (i = 0; i < filesId.length; i++) {

            html += '   <input type="hidden" name="files[]" value="' + filesId[i] 
+ '" />'

          }

        }

        if ($("#selectAllFiles").attr("checked")) {

          currentFolder = $("#folderTree li.active").attr("rel");

          if (isSearchResult) {

            currentFolder = currentFolder + "|" + isSearchResult + "|" + 
isGlobalSearch

          }

          html += '   <input type="hidden" name="currentFolder" value="' + 
currentFolder + '" />'

        }

        html += '   <ul class="main">';

        html += '       <li class="root active" rel="D0"><a href="#" 
class="highlight">root</a>' + list + "</li>";

        html += "   </ul>";

        html += '   <button type="submit">' + CMApplication.Dictionnary.MOVE + 
"</button>";

        html += '   <button type="reset" class="cancel">' + 
CMApplication.Dictionnary.CANCEL + "</button>";

        html += "</div></form>";

        CMApplication.Widgets.Dialog.displayContent(html, 450);

        $("#selectMoveDestination li.root li a 
em").replaceWith($("#selectMoveDestination li.root li a em").text());

        $("#selectMoveDestination li.root li.active").removeClass("active");

        $('#selectMoveDestination button[type="submit"]').click(function(e) {

          e.preventDefault();

          if ($("#selectMoveDestination li.active").length > 0) {

            $('#selectMoveDestinationForm 
input[name="destination"]').val($("#selectMoveDestination 
li.active").attr("rel"));

            $.post($("#selectMoveDestinationForm").attr("action"), 
$("#selectMoveDestinationForm").serialize(), function(data, textStatus, 
XMLHttpRequest) {

              currentFolder = $("#folderTree li.active").attr("rel");

              destinationFolder = data.data.destination != "root" ? 
data.data.destination : "D0";

              currentFolderIsDestination = data.data.destination == currentFolder 
|| (data.data.destination == "root" && currentFolder == "D0");

              if (data.status == "success" && !currentFolderIsDestination && 
!$("#selectAllFiles").attr("checked")) {

                for (i in data.data.files) {

                  $('#fileList li[rel="' + data.data.files[i] + '"]').remove();

                  if ($('#folderTree li:not(.collapse)[rel="' + destinationFolder 
+ '"]').length != 0) {

                    $('#folderTree li[rel="' + data.data.files[i] + 
'"]').appendTo('#folderTree li[rel="' + destinationFolder + '"] > ul')

                  } else {

                    $('#folderTree li[rel="' + data.data.files[i] + '"]').remove()

                  }

                }

                $("#selectAllFiles").attr("checked", false)

              } else {

                if ($("#selectAllFiles").attr("checked")) {

                  $("#fileList ul").empty()

                }

              }

              CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update();

              CMApplication.Widgets.Dialog.close();

              $("#selectAllFiles").attr("checked", false);

              $("#globalSearch").attr("checked", false)

            }, "json")

          }

        });

        $('#selectMoveDestination button[type="reset"]').click(function(e) {

          e.preventDefault();

          CMApplication.Widgets.Dialog.close()

        });

        $("#selectMoveDestination li").die("click");

        $("#selectMoveDestination li").live("click", function(e) {

          e.preventDefault();

          e.stopPropagation();

          $(this).toggleClass("collapse");

          if ($("ul", $(this)).length == 0) {

            
$(this).append(CMApplication.Widgets.FolderBrowser.browse($(this).attr("rel")))

          }

        });

        $("#selectMoveDestination li a").die("click");

        $("#selectMoveDestination li a").live("click", function(e) {

          e.preventDefault();

          $("#selectMoveDestination li.active").removeClass("active");

          $("#selectMoveDestination li a.highlight").removeClass("highlight");

          $(this).addClass("highlight");

          $(this).parent().addClass("active")

        })

      }, copy: function(filesId) {

        if ($("#selectAllFiles").attr("checked")) {

          if (typeof(totalItemCount) == "undefined") {

            totalItemCount = totalFilesInFolder

          }

          if (totalItemCount > 100) {

            if (!confirm("Are you sure you want to copy " + totalItemCount + " 
files?")) {

              return

            }

          }

        }

        if ($("#folderTree li.root > ul").length == 1) {

          $("#folderTree li.root ul script").remove();

          list = "<ul>" + $("#folderTree li.root > ul").html() + "</ul>"

        } else {

          list = CMApplication.Widgets.FolderBrowser.browse()

        }

        html = "<h4>" + CMApplication.Dictionnary.SELECT_A_DESTINATION + "</h4>";

        html += '<form id="selectCopyDestinationForm" action="' + 
CMApplication.URLs.languageFilesystemCopy + '"><div class="content folderTree" 
id="selectCopyDestination">';

        html += '   <input type="hidden" name="destination" value="" />';

        if (filesId != -1) {

          if (!$("#selectAllFiles").attr("checked")) {

            for (i = 0; i < filesId.length; i++) {

              html += '   <input type="hidden" name="files[]" value="' + 
filesId[i] + '" />'

            }

          }

          if ($("#selectAllFiles").attr("checked")) {

            currentFolder = $("#folderTree li.active").attr("rel");

            if (isSearchResult) {

              currentFolder = currentFolder + "|" + isSearchResult + "|" + 
isGlobalSearch

            }

            html += '   <input type="hidden" name="currentFolder" value="' + 
currentFolder + '" />'

          }

        } else {}

        html += '   <ul class="main">';

        html += '       <li class="root active" rel="D0"><a href="#" 
class="highlight">root</a>' + list + "</li>";

        html += "   </ul>";

        html += '   <button type="submit">' + CMApplication.Dictionnary.COPY + 
"</button>";

        html += '   <button type="reset" class="cancel">' + 
CMApplication.Dictionnary.CANCEL + "</button>";

        html += "</div></form>";

        CMApplication.Widgets.Dialog.displayContent(html, 450);

        $("#selectCopyDestination li.root li a 
em").replaceWith($("#selectCopyDestination li.root li a em").text());

        $("#selectCopyDestination li.root li.active").removeClass("active");

        $('#selectCopyDestination button[type="submit"]').click(function(e) {

          e.preventDefault();

          if ($("#selectCopyDestination li.active").length > 0) {

            $('#selectCopyDestinationForm 
input[name="destination"]').val($("#selectCopyDestination 
li.active").attr("rel"));

            $.post($("#selectCopyDestinationForm").attr("action"), 
$("#selectCopyDestinationForm").serialize(), function(data, textStatus, 
XMLHttpRequest) {

              currentFolder = $("#folderTree li.active").attr("rel");

              destinationFolder = data.data.destination != "root" ? 
data.data.destination : "D0";

              currentFolderIsDestination = data.data.destination == currentFolder 
|| (data.data.destination == "root" && currentFolder == "D0");

              if (data.status == "success") {

                if (currentFolderIsDestination) {

                  files = data.infos;

                  for (var i in files) {

                    file = files[i];

                    fileId = i;

                    CMApplication.Widgets.FileManager.Items._items["F" + fileId] = 
CMApplication.Widgets.FileManager.Items._items[file.originalFileId];

                    CMApplication.Widgets.FileManager.Items._items["F" + 
fileId].directory_id = jQuery.unparam(this.data).destination;

                    originalElement = $('#fileList li[rel="' + file.originalFileId 
+ '"]');

                    originalElement.clone().attr("rel", "F" + 
fileId).insertAfter(originalElement);

                    $('input[type="checkbox"]', originalElement).trigger("click");

                    $('#fileList li[rel="F' + fileId + '"] > a > 
span').text(file.name);

                    $('#fileList li[rel="F' + fileId + '"] > 
span.downloads').text("0");

                    $('#fileList li[rel="F' + fileId + '"] > input').val("F" + 
fileId);

                    var patt1 = new RegExp("[^/]+$");

                    $('#fileList li[rel="F' + fileId + '"] li a').each(function() 
{

                      $(this).attr("href", $(this).attr("href").replace(patt1, "F" 
+ fileId))

                    })

                  }

                  CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update()

                }

                CMApplication.Widgets.Dialog.close()

              } else {

                if (data.message == "space") {

                  CMApplication.Widgets.Dialog.displayUrl("/maximum-
storage?type=copy", 500)

                } else {

                  
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_C
OPY_UNABLE_TO_COPY + " #1", CMApplication.Widgets.Dialog.Types.error)

                }

              }

              $("#selectAllFiles").attr("checked", false);

              $("#globalSearch").attr("checked", false)

            }, "json")

          }

        });

        $('#selectCopyDestination button[type="reset"]').click(function(e) {

          e.preventDefault();

          CMApplication.Widgets.Dialog.close()

        });

        $("#selectCopyDestination li").die("click");

        $("#selectCopyDestination li").live("click", function(e) {

          e.preventDefault();

          e.stopPropagation();

          $(this).toggleClass("collapse");

          if ($("ul", $(this)).length == 0) {

            
$(this).append(CMApplication.Widgets.FolderBrowser.browse($(this).attr("rel")))

          }

        });

        $("#selectCopyDestination li a").die("click");

        $("#selectCopyDestination li a").live("click", function(e) {

          e.preventDefault();

          $("#selectCopyDestination li.active").removeClass("active");

          $("#selectCopyDestination li a.highlight").removeClass("highlight");

          $(this).addClass("highlight");

          $(this).parent().addClass("active")

        })

      }, newFolder: function(parentId) {

        
CMApplication.Widgets.Dialog.displayUrl(CMApplication.URLs.languageFilesystemCreat
e.replace(":parentId", parentId), 700);

        editForm = $("form", CMApplication.Widgets.Dialog.dialogContainer);

        $('select[name="parent_folder_id"]', editForm).val($("#folderTree 
li.active").attr("rel"));

        editForm.bind("successCallback", function(event, data) {

          if (data.status == "success") {

            
CMApplication.Widgets.FileManager.FileBrowser.FolderTree.createNode(data.infos)

          } else {

            CMApplication.Widgets.Dialog.displayMessage(data.messages.join("<br 
/>"), CMApplication.Widgets.Dialog.Types.error)

          }

        })

      }, trash: function(filesId) {

        var filesId;

        confirmation = 
confirm(CMApplication.Dictionnary.ARE_YOU_SURE_YOU_WANT_TO_DELETE_THESE_FILES);

        if (!confirmation) {

          return false

        }

        jQuery.ajax({

          url: CMApplication.URLs.languageFilesystemTrash,

          type: "post",

          async: false,

          data: {

            files: filesId

          }, dataType: "json",

          success: function(data, textStatus, XMLHttpRequest) {

            if (data.status == "success") {

              CMApplication.Widgets.FileManager.deleteSelectedElement = true;

              for (var i in data.data.files) {

                if (data.data.files[i] == $("#itemInfo").attr("rel")) {

                  delete 
CMApplication.Widgets.FileManager.Items._items[data.data.files[i]];

                  $('#folderTree li[rel="' + data.data.files[i] + 
'"]').parent().closest("li").children("a").trigger("click")

                }

                $('li[rel="' + data.data.files[i] + '"]').remove()

              }

            } else {

              
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_T
RASH_UNABLE_TO_TRASH + " #1", CMApplication.Widgets.Dialog.Types.error)

            }

            CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update()

          }

        })

      }, premiumGeneral: function(filesId, premium) {

        var add_msg;

        if ($("#selectAllFiles").attr("checked")) {

          if (typeof(totalItemCount) == "undefined") {

            totalItemCount = totalFilesInFolder

          }

          add_msg = " (" + totalItemCount + ")"

        } else {

          add_msg = ""

        }

        var q = (premium) ? 
CMApplication.Dictionnary.ARE_YOU_SURE_YOU_WANT_TO_SET_THESE_FILES_ONLY_PREMIUM : 
CMApplication.Dictionnary.ARE_YOU_SURE_YOU_WANT_TO_UNSET_THESE_FILES_ONLY_PREMIUM;

        var confirmation = confirm(q + add_msg);

        if (!confirmation) {

          return false

        }

        var filesId;

        var currentFolder = "";

        if (filesId != -1) {

          if ($("#selectAllFiles").attr("checked")) {

            currentFolder = $("#folderTree li.active").attr("rel");

            if (isSearchResult) {

              currentFolder = currentFolder + "|" + isSearchResult + "|" + 
isGlobalSearch

            }

          }

        }

        if (premium) {

          var link_el = "premium";

          var func_success = function(data, textStatus, XMLHttpRequest) {

            if (data.status == "success") {

              CMApplication.Widgets.FileManager.deleteSelectedElement = false;

              for (var i in data.data.files) {

                var a = $('#fileList li[rel="' + data.data.files[i] + '"] a');

                if (!a.hasClass("isPremiumOnly")) {

                  a.addClass("isPremiumOnly")

                }

              }

            } else {

              
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_P
REMIUM_UNABLE_TO_PREMIUM + " #1", CMApplication.Widgets.Dialog.Types.error)

            }

          }

        } else {

          var link_el = "unsetPremium";

          var func_success = function(data, textStatus, XMLHttpRequest) {

            if (data.status == "success") {

              CMApplication.Widgets.FileManager.deleteSelectedElement = false;

              for (var i in data.data.files) {

                $('#fileList li[rel="' + data.data.files[i] + '"] 
a').removeClass("isPremiumOnly")

              }

            } else {

              
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.FILESYSTEM_P
REMIUM_UNABLE_TO_PREMIUM + " #1", CMApplication.Widgets.Dialog.Types.error)

            }

          }

        }

        jQuery.ajax({

          url: $("#navigationBar li." + link_el + " a").attr("href"),

          type: "post",

          async: false,

          data: {

            files: filesId,

            currentFolder: currentFolder

          }, dataType: "json",

          success: func_success

        })

      }, premium: function(filesId) {

        CMApplication.Widgets.FileManager.FileBrowser.premiumGeneral(filesId, 1)

      }, unpremium: function(filesId) {

        CMApplication.Widgets.FileManager.FileBrowser.premiumGeneral(filesId, 0)

      }, FolderTree: {

        Events: {

          update: function(event) {

            event.stopPropagation();

            event.preventDefault();

            elementContainer = $(this).children("ul");

            if (elementContainer.length == 0) {

              $(this).append("<ul></ul>");

              elementContainer = $(this).children("ul")

            }

            url = $(this).children("a").attr("href");

            if (url === undefined) {

              url = location.href

            }

            $("#globalSearch").attr("checked", false);

            elementContainer.load(url + "?partial=folderTree&orderFoldersBy=" + 
$('#sortForm input[name="folder_field"]').val() + "&orderFoldersDirection=" + 
$('#sortForm input[name="folder_direction"]').val())

          }, toggleFolder: function(event) {

            event.stopPropagation();

            event.preventDefault();

            if (!$(event.target).is("li") && !$(this).hasClass("collapse")) {

              return

            }

            $(this).toggleClass("collapse");

            if (!$(event.target).is("li")) {

              return

            }

            if (!$(this).hasClass("collapse")) {

              $(this).trigger("update")

            }

          }

        }, createNode: function(infos) {

          elementContainer = $('#folderTree li[rel="D' + infos.parent_id + '"] > 
ul');

          if (elementContainer.length == 0) {

            elementContainer = $("ul").appendTo('#folderTree li[rel="D' + 
infos.parent_id + '"]')

          }

          items = {};

          items["D" + infos.id] = infos;

          CMApplication.Widgets.FileManager.Items.add(items);

          var today = new Date();

          var today_str = today.getFullYear() + "-" + (today.getMonth() + 1) + "-" 
+ today.getDay() + " " + today.getHours() + ":" + today.getMinutes() + ":" + 
today.getSeconds();

          return $('<li rel="D' + infos.id + '" class="collapse" data-date="' + 
today_str + '"><a href="' + 
CMApplication.URLs.languageFilesystemBrowse.replace(":folderId", "D" + 
infos.id).replace(/\\/\\:[a-z]*/gi, "") + '">' + infos.name + 
"</a></li>").appendTo(elementContainer)

        }, updateActiveElement: function(folderId) {

          $("#folderTree li.active > a").text($("#folderTree li.active > a 
em").text());

          $("#folderTree li.active").removeClass("active");

          $('#folderTree li[rel="' + folderId + '"]').addClass("active");

          $("#folderTree li.active > a").wrapInner("<em />")

        }, _init: function() {

          $("#folderTree li").live("update", 
CMApplication.Widgets.FileManager.FileBrowser.FolderTree.Events.update);

          $("#folderTree li").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FolderTree.Events.toggleFolder);

          $("#folderTree li a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.Events.browse);

          $("#folderTree li.premium").bind("click", function(event) {

            event.preventDefault()

          })

        }

      }, ItemInfo: {

        Item: {

          Events: {

            share: function(event) {

              event.preventDefault();

              var xHtml = "";

              jQuery.ajax({

                async: false,

                url: 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", ""),

                type: "post",

                data: {

                  id: $("#itemInfo").attr("rel")

                }, dataType: "html",

                success: function(data, textStatus, XMLHttpRequest) {

                  xHtml = data

                }

              });

              CMApplication.Widgets.Dialog.displayContent(xHtml);

              
$("#linksForm").submit(CMApplication.Widgets.FileManager.NavigationBar.GenerateLin
k.Events.submit)

            }, edit: function(event) {

              event.preventDefault();

              CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"));

              editForm = $("form", CMApplication.Widgets.Dialog.dialogContainer);

              editForm.bind("successCallback", function(event, data) {

                for (var key in data.data) {

                  if (key != "id") {

                    propertyExist = 
CMApplication.Widgets.FileManager.Items._items[data.data.id][key] != undefined;

                    if (propertyExist) {

                      
CMApplication.Widgets.FileManager.Items._items[data.data.id][key] = data.data[key]

                    }

                  }

                }

                
CMApplication.Widgets.FileManager.Items._items[data.data.id]["updated_on"] = 
"Now";

                CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update();

                $('#folderTree li[rel="' + data.data.id + '"] > a > 
em').text(data.data.name);

                $('#fileList li[rel="' + data.data.id + '"] > a 
span.fileName').text(data.data.name)

              })

            }, trash: function(event) {

              event.preventDefault();

              var fileId = new Array();

              if ($("#itemInfo").attr("rel").indexOf(",") !== -1) {

                fileId = $("#itemInfo").attr("rel").split(",")

              } else {

                fileId.push($("#itemInfo").attr("rel"))

              }

              CMApplication.Widgets.FileManager.FileBrowser.trash(fileId)

            }, editMultiple: function(event) {

              if ($("#selectAllFiles").attr("checked")) {

                if (typeof(totalItemCount) == "undefined") {

                  totalItemCount = totalFilesInFolder

                }

                if (totalItemCount > 100) {

                  if (!confirm("Are you sure you want to edit " + totalItemCount + 
" files?")) {

                    return

                  }

                }

                currentFolderVal = $("#folderTree li.active").attr("rel");

                if (isSearchResult) {

                  currentFolderVal = currentFolderVal + "|" + isSearchResult + "|" 
+ isGlobalSearch

                }

              } else {

                currentFolderVal = -1

              }

              event.preventDefault();

              elementsId = "";

              $("#fileList li.selected").each(function() {

                elementsId = elementsId + "," + ($(this).attr("rel"))

              });

              elementsId = elementsId.substring(1);

              CMApplication.Widgets.Dialog.displayUrl($(this).attr("href") + 
elementsId);

              editMultipleForm = $("form", 
CMApplication.Widgets.Dialog.dialogContainer);

              editMultipleForm.bind("successCallback", function(event, data) {

                if (data.status == "success") {

                  if ($("#selectAllFiles").attr("checked")) {

                    
setTimeout("CMApplication.Widgets.FileManager.FileBrowser.browse()", 500)

                  } else {

                    CMApplication.Widgets.FileManager.FileBrowser.browse()

                  }

                } else {

                  
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.ERROR, 
CMApplication.Widgets.Dialog.Types.error)

                }

              });

              $("#currentFolder").val(currentFolderVal)

            }

          }

        }, _init: function() {

          $("#itemInfo ul.action li.copy a").live("click", function(e) {

            e.preventDefault();

            id = new Array();

            if ($("#itemInfo").attr("rel").indexOf(",") !== -1) {

              id = $("#itemInfo").attr("rel").split(",")

            } else {

              id.push($("#itemInfo").attr("rel"))

            }

            CMApplication.Widgets.FileManager.FileBrowser.copy(id)

          });

          $("#itemInfo ul.action li.move a").live("click", function(e) {

            e.preventDefault();

            id = new Array();

            if ($("#itemInfo").attr("rel").indexOf(",") !== -1) {

              id = $("#itemInfo").attr("rel").split(",")

            } else {

              id.push($("#itemInfo").attr("rel"))

            }

            CMApplication.Widgets.FileManager.FileBrowser.move(id)

          });

          $("#itemInfo.isSelection ul.action li.edit a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.Item.Events.editMultiple);

          $("#itemInfo:not(.isSelection) ul.action li.edit a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.Item.Events.edit);

          $("#itemInfo ul.action li.trash a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.Item.Events.trash);

          $("#itemInfo ul.action li.share a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.Item.Events.share)

        }, getHumanReadableSize: function(size) {

          size = parseFloat(size);

          units = new Array();

          units.push("B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB");

          unit = units.shift();

          cnt = 0;

          now = new Date().getTime();

          while (size >= 1024) {

            if (++cnt > 8) {

              break

            }

            size = size / 1024;

            unit = units.shift()

          }

          result = (Math.round(size * 100) / 100).toString() + " " + unit;

          return result

        }, update: function() {

          switch ($("body#FileSystem_Index #fileList li input:checked").length) {

          case 0:

            
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.updateFolder($("#folderTree 
li.active").attr("rel"));

            break;

          case 1:

            
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.updateFile($("#fileList li 
input:checked").val());

            break;

          default:

            var ids = new Array();

            $("#fileList li input:checked").each(function() {

              ids.push($(this).val())

            });

            if (!$("#selectAllFiles").attr("checked")) {

              
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.updateFiles(ids)

            } else {

              
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.selectAllFiles(ids)

            }

            break

          }

        }, updateFolder: function(id) {

          if ("undefined" == (typeof id)) {

            return

          }

          if (id == "D0") {

            
$("#itemInfo").removeClass("isFile").removeClass("isSelection").addClass("isFolder
").html("").hide();

            return

          }

          fileInfo = CMApplication.Widgets.FileManager.Items.getInfo(id);

          xHtml = "";

          xHtml += '<strong class="label"><span>' + fileInfo.name + 
"</span></strong>";

          xHtml += '<ul class="action">';

          xHtml += '  <li class="move"><a href="' + 
CMApplication.URLs.languageFilesystemMove.replace(":id", id) + '" 
title="Move"><span>' + CMApplication.Dictionnary.MOVE + "</span></a>";

          xHtml += '  <li class="edit"><a href="' + 
CMApplication.URLs.languageFilesystemEdit.replace(":id", id) + '" 
title="Edit"><span>' + CMApplication.Dictionnary.EDIT + "</span></a>";

          xHtml += '  <li class="trash"><a href="' + 
CMApplication.URLs.languageFilesystemTrash.replace(":id", id) + '" 
title="Trash"><span>' + CMApplication.Dictionnary.TRASH + "</span></a>";

          xHtml += '  <li class="share"><a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", id) + '" 
title="Share"><span>' + CMApplication.Dictionnary.SHARE + "</span></a>";

          xHtml += "</ul>";

          if (typeof(totalItemCount) == "undefined") {

            totalItemCount = totalFilesInFolder

          }

          xHtml += '<div class="info">';

          xHtml += '    <span class="isPublic">' + (fileInfo.is_public == 1 ? 
"Public" : "Private") + "</span>";

          xHtml += '    <span class="contain">Contain ' + totalItemCount + " 
files</span>";

          xHtml += "</div>";

          if (fileInfo.description != "") {

            xHtml += '<div class="description">';

            xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DESCRIPTION + "</span>";

            xHtml += '    <span class="value">' + fileInfo.description + 
"</span>";

            xHtml += "</div>"

          }

          if (fileInfo.created_on != null) {

            xHtml += '<div class="createdOn">';

            xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DATE_CREATED + "</span>";

            xHtml += '    <span class="value">' + fileInfo.created_on + "</span>";

            xHtml += "</div>"

          }

          if (fileInfo.created_on != fileInfo.updated_on) {

            xHtml += '<div class="updatedOn">';

            xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DATE_UPDATED + "</span>";

            xHtml += '    <span class="value">' + fileInfo.updated_on + "</span>";

            xHtml += "</div>"

          }

          xHtml += '<div class="links">';

          if (fileInfo.is_public == 1) {

            url = "http://www.wupload.com/folder/" + (fileInfo.unique_id != "" ? 
fileInfo.unique_id : fileInfo.id);

            xHtml += "    <textarea>" + url + "</textarea>"

          } else {

            xHtml += "<em>" + CMApplication.Dictionnary.MUST_BE_PUBLIC + "</em>"

          }

          xHtml += "</div>";

          $("#itemInfo").attr("rel", 
id).removeClass("isFile").removeClass("isSelection").addClass("isFolder").html(xHt
ml).show()

        }, updateFile: function(id) {

          fileInfo = CMApplication.Widgets.FileManager.Items.getInfo(id);

          switch (fileInfo.source_id) {

          case 1:

            itemSource = CMApplication.Dictionnary.COPY;

            break;

          case 6:

          case 2:

            itemSource = CMApplication.Dictionnary.WEB_UPLOAD;

            break;

          case 3:

          case 4:

            itemSource = CMApplication.Dictionnary.REMOTE_UPLOAD;

            break;

          case 5:

            itemSource = "FTP";

            break;

          default:

            itemSource = CMApplication.Dictionnary.UNKNOWN

          }

          xHtml = "";

          xHtml += '<strong class="label"><span>' + fileInfo.name + 
"</span></strong>";

          xHtml += '<ul class="action">';

          xHtml += '  <li class="copy"><a href="' + 
CMApplication.URLs.languageFilesystemCopy.replace(":id", id) + '" 
title="Copy"><span>' + CMApplication.Dictionnary.COPY + "</span></a>";

          xHtml += '  <li class="move"><a href="' + 
CMApplication.URLs.languageFilesystemMove.replace(":id", id) + '" 
title="Move"><span>' + CMApplication.Dictionnary.MOVE + "</span></a>";

          xHtml += '  <li class="edit"><a href="' + 
CMApplication.URLs.languageFilesystemEdit.replace(":id", id) + '" 
title="Edit"><span>' + CMApplication.Dictionnary.EDIT + "</span></a>";

          xHtml += '  <li class="trash"><a href="' + 
CMApplication.URLs.languageFilesystemTrash.replace(":id", id) + '" 
title="Trash"><span>' + CMApplication.Dictionnary.TRASH + "</span></a>";

          xHtml += '  <li class="share"><a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", id) + '" 
title="Share"><span>' + CMApplication.Dictionnary.SHARE + "</span></a>";

          xHtml += '  <li class="download"><a href="' + 
CMApplication.URLs.languageDownload.replace(":id", id.replace("F", "")) + '" 
title="Download"><span>' + CMApplication.Dictionnary.DOWNLOAD_LINK + 
"</span></a>";

          xHtml += "</ul>";

          xHtml += '<div class="info">';

          xHtml += '    <span class="size">' + 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.getHumanReadableSize(fileIn
fo.size) + "</span>";

          if (fileInfo.premium_only == 1) {

            xHtml += '    <span class="premiumOnly">Premium Only</span>'

          }

          xHtml += '    <span class="password">' + (fileInfo.password != null && 
fileInfo.password != "" ? "Has password" : "No password") + "</span>";

          xHtml += '    <span class="source">Via ' + itemSource + "</span>";

          xHtml += "</div>";

          if (fileInfo.description != "") {

            xHtml += '<div class="description">';

            xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DESCRIPTION + "</span>";

            xHtml += '    <span class="value">' + fileInfo.description + 
"</span>";

            xHtml += "</div>"

          }

          xHtml += '<div class="createdOn">';

          xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DATE_CREATED + "</span>";

          xHtml += '    <span class="value">' + fileInfo.created_on + "</span>";

          xHtml += "</div>";

          if (fileInfo.created_on != fileInfo.updated_on) {

            xHtml += '<div class="updatedOn">';

            xHtml += '    <span class="field">' + 
CMApplication.Dictionnary.DATE_UPDATED + "</span>";

            xHtml += '    <span class="value">' + fileInfo.updated_on + "</span>";

            xHtml += "</div>"

          }

          xHtml += '<div class="links">';

          url = "http://www.wupload.com/file/" + fileInfo.id;

          xHtml += "    <textarea>" + url + "</textarea>";

          xHtml += "</div>";

          $("#itemInfo").attr("rel", 
id).removeClass("isFolder").removeClass("isSelection").addClass("isFile").html(xHt
ml).show()

        }, updateFiles: function(ids) {

          xHtml = "";

          xHtml += '<strong class="label"><span>' + ids.length + " files 
selected</span></strong>";

          totalSize = 0;

          for (i = 0; i < ids.length; i++) {

            fileInfo = CMApplication.Widgets.FileManager.Items.getInfo(ids[i]);

            totalSize += fileInfo.size

          }

          xHtml += '<ul class="action">';

          xHtml += '  <li class="copy"><a href="' + 
CMApplication.URLs.languageFilesystemCopy.replace(":id", "") + '" 
title="Copy"><span>' + CMApplication.Dictionnary.COPY + "</span></a>";

          xHtml += '  <li class="move"><a href="' + 
CMApplication.URLs.languageFilesystemMove.replace(":id", "") + '" 
title="Move"><span>' + CMApplication.Dictionnary.MOVE + "</span></a>";

          xHtml += '  <li class="edit"><a href="' + 
CMApplication.URLs.languageFilesystemEditMultiple.replace(":id", "") + '" 
title="Edit"><span>' + CMApplication.Dictionnary.EDIT + "</span></a>";

          xHtml += '  <li class="trash"><a href="' + 
CMApplication.URLs.languageFilesystemTrash.replace(":id", "") + '" 
title="Trash"><span>' + CMApplication.Dictionnary.TRASH + "</span></a>";

          xHtml += '  <li class="share"><a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", ids.join(",")) + 
'" title="Share"><span>' + CMApplication.Dictionnary.SHARE + "</span></a>";

          xHtml += "</ul>";

          xHtml += '<div class="info">';

          xHtml += '    <span class="size">' + 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.getHumanReadableSize(totalS
ize) + "</span>";

          xHtml += "</div>";

          xHtml += '<div class="links">';

          xHtml += "    <textarea>";

          $(ids).each(function() {

            xHtml += "http://www.wupload.com/file/" + this.replace("F", "") + "\\n"

          });

          xHtml += "</textarea>";

          xHtml += "</div>";

          $("#itemInfo").attr("rel", 
ids.join(",")).removeClass("isFolder").removeClass("isFile").addClass("isSelection
").html(xHtml).show()

        }, selectAllFiles: function(ids) {

          xHtml = "";

          var msg = "";

          if (typeof(totalItemCount) == "undefined") {

            totalItemCount = totalFilesInFolder

          }

          if (isSearchResult) {

            msg = totalItemCount + ' files selected<br>("' + isSearchResult + '" - 
search results)'

          } else {

            msg = totalItemCount + " files selected (full dir)"

          }

          xHtml += '<strong class="label"><span>' + msg + "</span></strong>";

          if (totalItemCount <= ids.length) {

            totalSize = 0;

            for (i = 0; i < ids.length; i++) {

              fileInfo = CMApplication.Widgets.FileManager.Items.getInfo(ids[i]);

              totalSize += fileInfo.size

            }

            xHtml += '<ul class="action">';

            xHtml += '  <li class="copy"><a href="' + 
CMApplication.URLs.languageFilesystemCopy.replace(":id", "") + '" 
title="Copy"><span>' + CMApplication.Dictionnary.COPY + "</span></a>";

            xHtml += '  <li class="move"><a href="' + 
CMApplication.URLs.languageFilesystemMove.replace(":id", "") + '" 
title="Move"><span>' + CMApplication.Dictionnary.MOVE + "</span></a>";

            xHtml += '  <li class="edit"><a href="' + 
CMApplication.URLs.languageFilesystemEditMultiple.replace(":id", "") + '" 
title="Edit"><span>' + CMApplication.Dictionnary.EDIT + "</span></a>";

            xHtml += '  <li class="trash"><a href="' + 
CMApplication.URLs.languageFilesystemTrash.replace(":id", "") + '" 
title="Trash"><span>' + CMApplication.Dictionnary.TRASH + "</span></a>";

            xHtml += '  <li class="share"><a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", ids.join(",")) + 
'" title="Share"><span>' + CMApplication.Dictionnary.SHARE + "</span></a>";

            xHtml += "</ul>";

            xHtml += '<div class="info">';

            xHtml += '    <span class="size">' + 
CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.getHumanReadableSize(totalS
ize) + "</span>";

            xHtml += "</div>";

            xHtml += '<div class="links">';

            xHtml += "    <textarea>";

            $(ids).each(function() {

              xHtml += "http://www.wupload.com/file/" + this.replace("F", "") + 
"\\n"

            });

            xHtml += "</textarea>";

            xHtml += "</div>";

            $("#itemInfo").attr("rel", 
ids.join(",")).removeClass("isFolder").removeClass("isFile").addClass("isSelection
").html(xHtml).show()

          } else {

            xHtml += '<ul class="action">';

            xHtml += '  <li class="copy"><a href="' + 
CMApplication.URLs.languageFilesystemCopy.replace(":id", "") + '" 
title="Copy"><span>' + CMApplication.Dictionnary.COPY + "</span></a>";

            xHtml += '  <li class="move"><a href="' + 
CMApplication.URLs.languageFilesystemMove.replace(":id", "") + '" 
title="Move"><span>' + CMApplication.Dictionnary.MOVE + "</span></a>";

            xHtml += '  <li class="edit"><a href="' + 
CMApplication.URLs.languageFilesystemEditMultiple.replace(":id", "") + '" 
title="Edit"><span>' + CMApplication.Dictionnary.EDIT + "</span></a>";

            xHtml += '  <li class="share"><a href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", ids.join(",")) + 
'" title="Share"><span>' + CMApplication.Dictionnary.SHARE + "</span></a>";

            xHtml += "</ul>";

            $("#itemInfo").attr("rel", 
ids.join(",")).removeClass("isFolder").removeClass("isFile").addClass("isSelection
").html(xHtml).show()

          }

        }

      }, FileList: {

        deleteSelectedElement: false,

        Item: {

          Events: {

            share: function(event) {

              event.preventDefault();

              var xHtml = "";

              jQuery.ajax({

                async: false,

                url: $(this).attr("href"),

                type: "GET",

                dataType: "html",

                success: function(data, textStatus, XMLHttpRequest) {

                  xHtml = data

                }

              });

              CMApplication.Widgets.Dialog.displayContent(xHtml);

              
$("#linksForm").submit(CMApplication.Widgets.FileManager.NavigationBar.GenerateLin
k.Events.submit)

            }, edit: function(event) {

              event.preventDefault();

              CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"));

              editForm = $("form", CMApplication.Widgets.Dialog.dialogContainer);

              editForm.bind("successCallback", function(event, data) {

                items = {};

                items["F" + data.infos.id] = data.infos;

                CMApplication.Widgets.FileManager.Items.add(items);

                CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update();

                $('#fileList li[rel="F' + data.infos.id + '"] > a 
span').text(data.infos.name)

              })

            }, copy: function(event) {

              event.preventDefault();

              var ids = new Array($(this).parents("li[rel]").attr("rel"));

              CMApplication.Widgets.FileManager.FileBrowser.copy(ids)

            }, move: function(event) {

              event.preventDefault();

              var ids = new Array($(this).parents("li[rel]").attr("rel"));

              CMApplication.Widgets.FileManager.FileBrowser.move(ids)

            }, trash: function(event) {

              event.preventDefault();

              var fileId = new Array();

              fileId[0] = $(this).closest("#fileList > ul > li").attr("rel");

              CMApplication.Widgets.FileManager.FileBrowser.trash(fileId)

            }, premium: function(event) {

              event.preventDefault();

              var fileId = new Array();

              fileId[0] = $(this).closest("#fileList > ul > li").attr("rel");

              CMApplication.Widgets.FileManager.FileBrowser.premium(fileId)

            }

          }, _init: function() {

            $("#fileList ul.fileAction li.copy a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.copy);

            $("#fileList ul.fileAction li.move a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.move);

            $("#fileList ul.fileAction li.share a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.share);

            $("#fileList ul.fileAction li.edit a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.edit);

            $("#fileList ul.fileAction li.trash a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.trash);

            $("#fileList ul.fileAction li.premium a").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Item.Events.premium)

          }

        }, createNode: function(id, name, isDir, size, downloads, extension) {

          elementContainer = $("#fileList > ul");

          xhtml = "";

          xhtml += '<li rel="' + id + '"' + (isDir ? ' class="folder"' : "") + 
">\\n";

          xhtml += '    <input type="checkbox" class="select" value="' + id + '" 
/>\\n';

          xhtml += "    <a" + (!isDir ? ' class="ext_' + extension + '"' : "") + 
"><span>" + name + "</span></a>\\n";

          xhtml += '    <span class="size">' + size + "</span>\\n";

          xhtml += '    <span class="downloads">' + (!isDir ? downloads : 
"&nbsp;") + "</span>\\n";

          xhtml += '    <ul class="fileAction">\\n';

          xhtml += '        <li class="share"><a title="' + 
CMApplication.Dictionnary.SHARE + '" href="' + 
CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", id) + '">' + 
CMApplication.Dictionnary.SHARE + "</a></li>\\n";

          xhtml += '        <li class="edit"><a title="' + 
CMApplication.Dictionnary.EDIT + '" href="' + 
CMApplication.URLs.languageFilesystemEdit.replace(":id", id) + '">' + 
CMApplication.Dictionnary.EDIT + "</a></li>\\n";

          xhtml += '        <li class="trash"><a title="' + 
CMApplication.Dictionnary.TRASH + '" href="' + 
CMApplication.URLs.languageFilesystemTrash.replace(":id", id) + '">' + 
CMApplication.Dictionnary.TRASH + "</a></li>\\n";

          xhtml += "    </ul>\\n";

          if (!isDir) {

            newElement = $(xhtml).appendTo(elementContainer)

          } else {

            newElement = $(xhtml).prependTo(elementContainer)

          }

          return newElement

        }, populate: function(content, folderId) {

          $("#fileList").html(content);

          $(".navigationHelper .paginator").replaceWith($("#fileList .paginator"))

        }, Selection: function(event, selectAll) {

          isOriginalCheckboxClick = event.clientX !== undefined;

          if ((isOriginalCheckboxClick && $(this).is(":checked")) || 
(!isOriginalCheckboxClick && !$(this).is(":checked"))) {

            $(this).parent("li").addClass("selected");

            $("#selectAllFolder").attr("checked", false)

          } else {

            $("#selectAllFiles").attr("checked", false);

            $(this).parent("li").removeClass("selected")

          }

          CMApplication.Widgets.FileManager.NavigationBar.updateLinksStyles();

          if (selectAll !== true) {

            
setTimeout("CMApplication.Widgets.FileManager.FileBrowser.ItemInfo.update()", 1)

          }

        }, _init: function() {

          $("#fileList > ul > li:has(input.select:checked)").addClass("selected");

          $("#fileList > ul > li input.select").live("click", 
CMApplication.Widgets.FileManager.FileBrowser.FileList.Selection);

          $("#fileList > ul > li").live("mousedown", function(event) {

            if ($(event.target).is("li") || $(event.target).is("#fileList > ul > 
li > a, #fileList > ul > li > a span")) {

              $("input.select", this).click()

            }

          });

          CMApplication.Widgets.FileManager.NavigationHelper.sortBy.update()

        }

      }

    }, adjustFileBrowserHeight: function() {

      fileManagerHeight = $(window).height();

      $("#fileManager").css("height", fileManagerHeight);

      fileBrowserHeight = fileManagerHeight - ($("#fileBrowser").outerHeight() - 
$("#fileBrowser").height());

      $("#fileManager > *:not(#fileBrowser)").each(function() {

        fileBrowserHeight -= $(this).outerHeight()

      });

      if (fileBrowserHeight < 200) {

        fileBrowserHeight = 200;

        $("#fileManager").css("height", fileManagerHeight + fileBrowserHeight)

      }

      $("#fileBrowser").css("height", fileBrowserHeight);

      $("#fileBrowser").css("display", "block")

    }, _init: function() {

      CMApplication.Widgets.FileManager.FileBrowser.ItemInfo._init();

      CMApplication.Widgets.FileManager.FileBrowser.FileList._init();

      CMApplication.Widgets.FileManager.FileBrowser.FileList.Item._init();

      CMApplication.Widgets.FileManager.FileBrowser.FolderTree._init();

      CMApplication.Widgets.FileManager.NavigationBar._init();

      CMApplication.Widgets.FileManager.NavigationHelper._init();

      CMApplication.Widgets.FileManager.adjustFileBrowserHeight();

      if ($("#fileManager").length == 1) {

        window.location.href = "#fileManager"

      }

      $("#fileManager > .exportLinks a").live("click", function(e) {

        e.preventDefault();

        if ($(this).is("#exportFolderLinks")) {

          url = 
CMApplication.URLs.languageFilesystemExportFolderLinks.replace(":folderId", 
$("#folderTree li.active").attr("rel").replace("D", "")) + "/" + 
$("#typeExport").val()

        } else {

          url = $(this).attr("href") + "/-1/" + $("#typeExport").val()

        }

        window.open(url)

      })

    }

  };

  CMApplication.Widgets.Login = {

    widgetLink: $("#lMainUsage li.login a:not(.active,.signup,.lang)"),

    widgetContainer: $("#loginWidget"),

    Events: {

      open: function(e) {

        e.preventDefault();

        if (!$(this).hasClass("active")) {

          e.stopPropagation();

          CMApplication.Widgets.Login.open(this)

        }

      }, close: function(e) {

        clickedElement = $(e.target);

        isChild = 
CMApplication.Widgets.Login.widgetContainer.has(clickedElement).length > 0;

        isSame = CMApplication.Widgets.Login.widgetContainer[0] === 
clickedElement[0];

        if (!isChild && !isSame) {

          e.preventDefault();

          CMApplication.Widgets.Login.close()

        }

      }, submit: function(e) {

        e.preventDefault();

        CMApplication.Widgets.Login.submit($(this))

      }

    }, open: function() {

      this.widgetLink.addClass("active");

      this.widgetContainer.show();

      $(document).bind("click", this.Events.close)

    }, close: function() {

      this.widgetContainer.hide();

      this.widgetLink.removeClass("active");

      $(document).unbind("click", this.Events.close)

    }, submit: function(form) {

      jQuery.ajax({

        data: form.serialize(),

        dataType: "json",

        cache: false,

        url: form.attr("action"),

        type: form.attr("method"),

        success: function(data, textStatus, XMLHttpRequest) {

          try {

            if (data.status == "success") {

              if ($.browser.webkit) {

                $("form", 
CMApplication.Widgets.Login.widgetContainer).unbind("submit");

                $("form", CMApplication.Widgets.Login.widgetContainer).submit()

              } else {

                if (data.redirect) {

                  CMApplication.foward(data.redirect)

                }

              }

            } else {

              msg = CMApplication.Dictionnary.UNEXPECTED_PROCESS_ERROR + "\\n\\n";

              for (var field in data.messages) {

                msg += field + ":\\n";

                value = data.messages[field];

                if (typeof(value) === "object") {

                  for (var subfield in value) {

                    msg += "    - " + value[subfield] + "\\n"

                  }

                } else {

                  msg += "    - " + value + "\\n"

                }

              }

              CMApplication.Widgets.Dialog.displayMessage(msg, 
CMApplication.Widgets.Dialog.Types.error)

            }

          } catch(e) {

            if (e == "d is null") {

              e = e + " (" + textStatus + ") / " + XMLHttpRequest.responseText

            }

            
CMApplication.Widgets.Dialog.displayMessage(CMApplication.Dictionnary.LOGIN_UNEXPE
CTED_PROCESS_ERROR + " #1" + e, CMApplication.Widgets.Dialog.Types.exception)

          }

        }

      })

    }, decode: function(input) {

      var _keyStr = 
"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

      var output = "";

      var chr1, chr2, chr3;

      var enc1, enc2, enc3, enc4;

      var i = 0;

      input = input.replace(/[^A-Za-z0-9\\+\\/\\=]/g, "");

      while (i < input.length) {

        enc1 = _keyStr.indexOf(input.charAt(i++));

        enc2 = _keyStr.indexOf(input.charAt(i++));

        enc3 = _keyStr.indexOf(input.charAt(i++));

        enc4 = _keyStr.indexOf(input.charAt(i++));

        chr1 = (enc1 << 2) | (enc2 >> 4);

        chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);

        chr3 = ((enc3 & 3) << 6) | enc4;

        output = output + String.fromCharCode(chr1);

        if (enc3 != 64) {

          output = output + String.fromCharCode(chr2)

        }

        if (enc4 != 64) {

          output = output + String.fromCharCode(chr3)

        }

      }

      return output

    }, _init: function() {

      CMApplication.Widgets.Login.widgetLink.bind("click", 
CMApplication.Widgets.Login.Events.open);

      $("form", CMApplication.Widgets.Login.widgetContainer).bind("submit", 
CMApplication.Widgets.Login.Events.submit)

    }

  };

  jQuery.extend(CMApplication.Bootstrap, {

    _initPremiumPurchase: CMApplication.Widgets.Purchase._init,

    _initUser: function() {

      CMApplication.User.sessId = jQuery.getCookie("PHPSESSID");

      CMApplication.User.email = jQuery.getCookie("email");

      CMApplication.User.isAffiliate = jQuery.getCookie("isAffiliate") == 1;

      if (jQuery.getCookie("role") == CMApplication.User.RolesNames[2]) {

        CMApplication.User.role = CMApplication.User.RolesNames[2]

      } else {

        if (jQuery.getCookie("role") == CMApplication.User.RolesNames[1]) {

          CMApplication.User.role = CMApplication.User.RolesNames[1]

        } else {

          CMApplication.User.role = CMApplication.User.RolesNames[0]

        }

      }

    }, _initLayout: CMApplication.Layout._init,

    _initLoginWidget: CMApplication.Widgets.Login._init,

    _initInternationalizationWidget: function() {

      CMApplication.Widgets.Internationalization.widgetLink.bind("click", 
CMApplication.Widgets.Internationalization.Events.open)

    }, _initViewportAdjustment: function() {

      CMApplication.Viewport.adjust();

      window.onresize = CMApplication.Viewport.adjust

    }, _initAdvancedUpload: CMApplication.Widgets.AdvancedUpload._init,

    _initUpload: CMApplication.Widgets.Upload._init,

    _initFileManager: CMApplication.Widgets.FileManager._init,

    _initDownload: CMApplication.Pages.Download._init,

    _initToolsUserMenu: CMApplication.Widgets.Tools._init,

    _initStatsUserMenu: CMApplication.Widgets.Stats._init,

    _initStats: function() {

      $("#use_points").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl(this.href, undefined, 
"inlineStyle", event.target);

        $("#DialogWidgetContent #upgradeAccount form").die("successCallback");

        $("#DialogWidgetContent #upgradeAccount form").die("failCallback");

        $("#DialogWidgetContent #upgradeAccount form").live("successCallback", 
function() {

          alert("Completed, thank you")

        });

        $("#DialogWidgetContent #upgradeAccount form").live("failCallback", 
function(a, b) {

          alert("Error while executing request:\\n\\n- " + b.messages.join("\\n- "))

        })

      });

      $("#statisticSales a").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl(this.href, 600, "inlineStyle", 
event.target)

      })

    }, _initFaq: function() {

      $('body#Support_Faq .CL3 a[href^="#"], body#Support_Faq .CL3 a[href^="' + 
window.location.href.replace(window.location.hash, "") + '#"]').live("click", 
function(e) {

        e.preventDefault();

        
$($(this).attr("href").replace(window.location.href.replace(window.location.hash, 
""), "")).toggleClass("odd")

      })

    }, _initNews: function() {

      $("body#News_Index #newsPosts h3").live("click", function(e) {

        e.preventDefault();

        $(this).parent().toggleClass("openPost")

      })

    }, _initDialog: CMApplication.Widgets.Dialog._init,

    _initGenerateLink: function() {

      $("#DialogWidgetContent .fileLinks a,#DialogWidgetContent .emailLinks 
a").live("click", function(e) {

        e.preventDefault();

        files = new Array();

        $('input[name="id[]"]').each(function(index) {

          files[index] = $(this).val()

        });

        jQuery.ajax({

          url: $(this).attr("href"),

          type: "post",

          async: false,

          data: {

            files: files.join(",")

          }, dataType: "html",

          success: function(data, textStatus, XMLHttpRequest) {

            CMApplication.Widgets.Dialog.displayContent(data)

          }

        })

      });

      $("#linksForm textarea, #linksForm input").live("focus", function() {

        $(this).select()

      });

      $("#linksForm #outputType, #linksForm #selectFileName, #linksForm 
#domainName").live("change", function(e) {

        files = new Array();

        $('input[name="id[]"]').each(function(index) {

          files[index] = $(this).val()

        });

        jQuery.ajax({

          url: CMApplication.URLs.languageFilesystemGenerateLink.replace(":id", 
files.join(",")),

          type: "post",

          async: false,

          data: {

            id: files.join(","),

            outputType: $("#outputType").val(),

            selectFileName: $("#selectFileName").val()

          }, dataType: "html",

          success: function(data, textStatus, XMLHttpRequest) {

            CMApplication.Widgets.Dialog.displayContent(data)

          }

        })

      })

    }, _initManageFilesHelp: function() {

      $("#fileManager p.help a").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"), 900)

      })

    }, _initManageSecurityQuestions: function() {

      $("#User_Settings .securityQuestion, #User_Settings 
.securityQuestionModify").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"), 500)

      })

    }, _initHelp: function() {

      $("a.help").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl($(this).attr("href"), undefined, 
"inlineStyle", event.target)

      })

    }, _initMaximumStorage: function() {

      $(".maximumStorage").live("click", function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl("/maximum-storage", 500)

      })

    }, _initAffiliatePlanA: function() {

      $("#Affiliates_Index #affiliatePlans a.affiliatePlanA").live("click", 
function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl(this.href, 636, "defaultStyle 
affiliatePlanA")

      })

    }, _initAffiliatePlanB: function() {

      $("#Affiliates_Index #affiliatePlans a.affiliatePlanB").live("click", 
function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl(this.href, 636, "defaultStyle 
affiliatePlanB ")

      })

    }, _initAffiliatePlanC: function() {

      $("#Affiliates_Index #affiliatePlans a.affiliatePlanC").live("click", 
function(event) {

        event.preventDefault();

        CMApplication.Widgets.Dialog.displayUrl(this.href, 900, "defaultStyle 
affiliatePlanC ")

      })

    }

  });

  $("body.FileSystem div.paginator a").live("click", function(event) {

    if (window.location.href.indexOf(CMApplication.URLs.languageFilesystemRemoved) 
== -1) {

      event.preventDefault();

      currentPage = parseInt($(this).siblings('input[name="page"]').val());

      if ($(this).hasClass("previous")) {

        if (currentPage > 1) {

          $(this).siblings('input[name="page"]').val(currentPage - 1);

          CMApplication.Widgets.FileManager.FileBrowser.browse()

        }

      } else {

        if ($(this).hasClass("next")) {

          if (currentPage < parseInt($(this).siblings(".total").text())) {

            $(this).siblings('input[name="page"]').val(currentPage + 1);

            CMApplication.Widgets.FileManager.FileBrowser.browse()

          }

        } else {

          if ($(this).hasClass("first")) {

            if (currentPage > 1) {

              $(this).siblings('input[name="page"]').val(1);

              CMApplication.Widgets.FileManager.FileBrowser.browse()

            }

          } else {

            if ($(this).hasClass("last")) {

              var last = parseInt($(this).siblings(".total").text());

              if (currentPage < last) {

                $(this).siblings('input[name="page"]').val(last);

                CMApplication.Widgets.FileManager.FileBrowser.browse()

              }

            }

          }

        }

      }

    } else {

      return true

    }

  });

  $('body.FileSystem div.paginator input[name="page"]').live("change", 
function(event) {

    if (window.location.href.indexOf(CMApplication.URLs.languageFilesystemRemoved) 
== -1) {

      event.preventDefault();

      CMApplication.Widgets.FileManager.FileBrowser.browse()

    } else {

      return true

    }

  });

  CMApplication.Bootstrap.run()

});

window.onbeforeunload = function(a) {

  message = null;

  try {

    if ($("iframe.webUploadProxy").length || $("iframe.upload").length) {

      if (typeof a == "undefined") {

        a = window.event

      }

      if (a) {

        a.returnValue = CMApplication.Dictionnary.LEAVING_WILL_CANCEL_UPLOADS

      }

      return message

    }

  } catch(b) {}

};




function sortList(c) {

  var b = document.getElementById(c);

  for (var e in b.childNodes) {

    var a = b.childNodes[e];

    for (var d in b.childNodes) {

      var f = b.childNodes[d];

      if ((a.innerText != "undefined" || f.innerText != "undefined") && 
a.innerText > f.innerText) {

        if (b.firstChild != a) {

          b.insertBefore(f, a)

        }

      }

    }

  }

};
`;