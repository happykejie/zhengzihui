
$.extend(validatePrompt, {
    realname: {
        onFocus: "2-20λ�ַ����������Ļ�Ӣ�����",
        succeed: "",
        isNull: "��������ϵ������",
        error: {
            badLength: "��ϵ����������ֻ����2-20λ�ַ�֮��",
            badFormat: "��ϵ������ֻ�������Ļ�Ӣ�����"
        }
    },
    department: {
        onFocus: "",
        succeed: "",
        isNull: "��ѡ����ϵ�����ڲ���",
        error: ""
    },
    tel: {
        onFocus: "<span>����д��ϵ�˳��õĵ绰���Ա���������ϵ���磺0527-88105500</span>",
        succeed: "",
        isNull: "��������ϵ�˹̶��绰",
        error: "�绰��ʽ��������������"
    },
    mobile: {
        onFocus: "����д�����ֻ��ţ������Ϣ�Զ���֪ͨ",
        succeed: "",
        isNull: "",
        error: "�ֻ������ʽ������������ȷ���ֻ���"
    },
    companyname: {
        onFocus: "<span>����д���̾�ע���ȫ�ơ�4-40λ�ַ���������Ӣ�ġ����ּ���_������-����()���������</span>",
        succeed: "",
        isNull: "�����빫˾����",
        error: {
            badLength: "��˾���Ƴ���ֻ����4-40λ�ַ�֮��",
            badFormat: "<span>��˾����ֻ�������ġ�Ӣ�ġ����ּ���_������-����()���������</span>"
        }
    },
    companyarea: {
        onFocus: "��ѡ��˾���ڵ�",
        succeed: "",
        isNull: "��ѡ��˾���ڵ�",
        error: ""
    },
    companyaddr: {
        onFocus: "��������ׯ���ÿ������ƴ�ʮһ��18��ԺB��14��",
        succeed: "",
        isNull: "�����빫˾��ַ",
        error: {
            badLength: "��˾��ַ����ֻ����4-50λ�ַ�֮��",
            badFormat: "<span>��˾��ַֻ�������ġ�Ӣ�ġ����ּ���_������-����()��������#���</span>"
        }
    },
    purpose: {
        onFocus: "",
        succeed: "",
        isNull: "��ѡ��������/��;",
        error: ""
    },
    mobileCode: {
        onFocus: "",
        succeed: "",
        isNull: "�����������֤��",
        error: ""
    },
    companysite: {
        onFocus: "����д�����ͻ������ֻ���",
        succeed: "",
        isNull: "",
        error: ""
    },
    mail: {
        onFocus: "����д�������䣬�����Ϣ���ʼ�֪ͨ",
        succeed: "",
        isNull: "����������",
        error: {
            beUsed: "�������ѱ�ʹ�ã��������������",
            badFormat: "��������Ч�������ַ",
            badLength: "����д����������������ַֻ����50���ַ�����"
        }
    }
});
var emailstate=false
var emailold="";
$.extend(validateFunction, {
    mail: function (option) {
        var format = validateRules.isEmail(option.value);
        var format2 = validateRules.betweenLength(option.value, 0, 50);
        if (!format) {
            validateSettings.error.run(option, option.prompts.error.badFormat);
        } else {
            if (!format2) {
                validateSettings.error.run(option, option.prompts.error.badLength);
            } else {
                if (!emailstate || emailold != option.value) {
                    if (emailold != option.value) {
                        emailold = option.value;
                        validateSettings.succeed.run(option);
                        emailstate = true;
                    }
                    else {
                        validateSettings.error.run(option, option.prompts.error.beUsed);
                        emailstate = false;
                    }
                }
                else {
                    if ($("#email_linker")) {
                        $("#email_linker").text(option.value);
                    }
                    validateSettings.succeed.run(option);
                }
            }
        }
    },

    realname: function (option) {
        var length = validateRules.betweenLength(option.value.replace(/[^\x00-\xff]/g, "**"), 2, 20);
        var format = validateRules.isRealName(option.value);
        if (!length) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        } else {
            if (!format) {
                validateSettings.error.run(option, option.prompts.error.badFormat);
            }
            else {
                validateSettings.succeed.run(option);
            }
        }
    },
    department: function (option) {
        var bool = (option.value == -1);
        if (bool) {
            validateSettings.isNull.run(option, "");
        }
        else {
            validateSettings.succeed.run(option);
        }
    },
    tel: function (option) {
        var format = validateRules.isTel(option.value);
        if (!format) {
            validateSettings.error.run(option, option.prompts.error);
        }
        else {
            validateSettings.succeed.run(option);
        }
    },
    mobile: function (option) {
        var format = validateRules.isMobile(option.value);
        if (!format) {
            validateSettings.error.run(option, option.prompts.error);
        }
        else {
            validateSettings.succeed.run(option);
        }
    },
    companyname: function (option) {
        var length = validateRules.betweenLength(option.value.replace(/[^\x00-\xff]/g, "**"), 4, 40);
        var format = validateRules.isCompanyname(option.value);
        if (!length) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        }
        else {
            if (!format) {
                validateSettings.error.run(option, option.prompts.error.badFormat);
            } else {
                validateSettings.succeed.run(option);
            }
        }
    },
    companyarea: function (option) {
        var bool = (option.value == -1);
        if (bool) {
            validateSettings.isNull.run(option, "");
        }
        else {
            validateSettings.succeed.run(option);
        }
    },
    companyaddr: function (option) {
        var length = validateRules.betweenLength(option.value.replace(/[^\x00-\xff]/g, "**"), 4, 50);
        var format = validateRules.isCompanyaddr(option.value);
        if (!length) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        } else {
            if (!format) {
                validateSettings.error.run(option, option.prompts.error.badFormat);
            }
            else {
                validateSettings.succeed.run(option);
            }
        }
    },
    purpose: function (option) {
        var purpose = $("input:checkbox[@name='purposetype']");
        if (validateFunction.checkGroup(purpose)) {
            validateSettings.succeed.run(option);
        } else {
            validateSettings.error.run(option, option.prompts.isNull);
        }
    },
    companysite: function (option) {
    	var length = validateRules.betweenLength(option.value.replace(/[^\x00-\xff]/g, "**"), 2, 20);
//        var format = validateRules.isRealName(option.value);
        if (!length) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        } else {
//            if (!format) {
//                validateSettings.error.run(option, option.prompts.error.badFormat);
//            }
//            else {
                validateSettings.succeed.run(option);
//            }
        }
    },
    emRegCompany_validate: function () {
        if ($("#mobileCodeDiv").attr("class") == 'item') {
            $("#regName").jdValidate(validatePrompt.regName, validateFunction.regName, true);
            $("#pwd").jdValidate(validatePrompt.pwd, validateFunction.pwd, true)
            $("#pwdRepeat").jdValidate(validatePrompt.pwdRepeat, validateFunction.pwdRepeat, true);
            $("#realname").jdValidate(validatePrompt.realname, validateFunction.realname, true);
            $("#department").jdValidate(validatePrompt.department, validateFunction.department, true);
            $("#tel").jdValidate(validatePrompt.tel, validateFunction.tel, true);
            $("#companyname").jdValidate(validatePrompt.companyname, validateFunction.companyname, true);
            $("#hncompanyarea").jdValidate(validatePrompt.companyarea, validateFunction.companyarea, true);
            $("#companyaddr").jdValidate(validatePrompt.companyaddr, validateFunction.companyaddr, true);

            $("#purpose").jdValidate(validatePrompt.purpose, validateFunction.purpose, true);
            $("#mobileCode").jdValidate(validatePrompt.mobileCode, validateFunction.mobileCode, true);
            return validateFunction.FORM_submit(["#regName", "#pwd", "#pwdRepeat", "#realname", "#department", "#tel", "#companyname", "#hncompanyarea", "#companyaddr", "#purpose", "#mobileCode"]);
        } else {
            $("#regName").jdValidate(validatePrompt.regName, validateFunction.regName, true);
            $("#pwd").jdValidate(validatePrompt.pwd, validateFunction.pwd, true)
            $("#pwdRepeat").jdValidate(validatePrompt.pwdRepeat, validateFunction.pwdRepeat, true);
            $("#realname").jdValidate(validatePrompt.realname, validateFunction.realname, true);
            $("#department").jdValidate(validatePrompt.department, validateFunction.department, true);
            $("#tel").jdValidate(validatePrompt.tel, validateFunction.tel, true);

            $("#companyname").jdValidate(validatePrompt.companyname, validateFunction.companyname, true);
            $("#hncompanyarea").jdValidate(validatePrompt.companyarea, validateFunction.companyarea, true);
            $("#companyaddr").jdValidate(validatePrompt.companyaddr, validateFunction.companyaddr, true);
            $("#purpose").jdValidate(validatePrompt.purpose, validateFunction.purpose, true);
            
            return validateFunction.FORM_submit(["#regName", "#pwd", "#pwdRepeat", "#realname", "#department", "#tel", "#companyname", "#hncompanyarea", "#companyaddr", "#purpose"]);
        }
    }
});


$("#pwd").bind("keyup",
    function () {
        validateFunction.pwdstrength();
    }).jdValidate(validatePrompt.pwd, validateFunction.pwd)
$("#pwdRepeat").jdValidate(validatePrompt.pwdRepeat, validateFunction.pwdRepeat);
//$("#authcode").jdValidate(validatePrompt.authcode, validateFunction.authcode);
$("#regName").jdValidate(validatePrompt.regName, validateFunction.regName);

$("#realname").jdValidate(validatePrompt.realname, validateFunction.realname);
$("#department").jdValidate(validatePrompt.department, validateFunction.department);
$("#tel").jdValidate(validatePrompt.tel, validateFunction.tel);
$("#mobile").jdValidate(validatePrompt.mobile, validateFunction.mobile);
$("#mail").jdValidate(validatePrompt.mail, validateFunction.mail);

$("#companyname").jdValidate(validatePrompt.companyname, validateFunction.companyname);
$("#hncompanyarea").jdValidate(validatePrompt.companyarea, validateFunction.companyarea);
$("#companyaddr").jdValidate(validatePrompt.companyaddr, validateFunction.companyaddr);
//$("#companysite").jdValidate(validatePrompt.companysite, validateFunction.companysite);
$("#mobileCode").jdValidate(validatePrompt.mobileCode, validateFunction.mobileCode);

$("#viewpwd").bind("click", function () {
    if ($(this).attr("checked") == true) {
        validateFunction.showPassword("text");
        $("#o-password").addClass("pwdbg");
    } else {
        validateFunction.showPassword("password");
        $("#o-password").removeClass("pwdbg");
    }
});

$("select[@name2='hncompanyarea']").bind("change", function () {
    var elements = $("select[@name2='hncompanyarea']");
    if (validateFunction.checkSelectGroup(elements)) {
        $("#hncompanyarea").val("1");
        $("#hncompanyarea").attr("sta", 2);
        $("#hncompanyarea_error").html("");
        $("#hncompanyarea_error").removeClass();
        $("#hncompanyarea_succeed").addClass("succeed");
    } else {
        $("#hncompanyarea").val("-1");
        $("#hncompanyarea").attr("sta", 0);
        $("#hncompanyarea_error").html("");
        $("#hncompanyarea_succeed").removeClass("succeed");
    }
});

$("input:checkbox[@name='purposetype']").bind("click", function () {
    var value1 = $("#purpose").val();
    var value2 = $(this).val();
    if ($(this).attr("checked") == true) {
        if (value1.indexOf(value2) == -1) {
            $("#purpose").val(value1 + value2);
            $("#purpose").attr("sta", 2);
            $("#purpose_error").html("");
            $("#purpose_error").removeClass();
            $("#purpose_succeed").addClass("succeed");
        }
    } else {
        if (value1.indexOf(value2) != -1) {
            value1 = value1.replace(value2, "");
            $("#purpose").val(value1);
            if ($("#purpose").val() == "") {
                $("#purpose").attr("sta", 0);
                $("#purpose_succeed").removeClass("succeed");
            }
        }
    }
});

function protocolReg() {
    $("#closeBox").click();
    $("#registsubmit").click();
}

$("#registsubmit").click(function () {
	var mobileCodeFlag = false;
    var agreeProtocol = checkReadMe();
    var regnameOk = validateRegName();
	var mobile = $("#mobile").val();
    if (mobile == "") {
		$('#mobile').addClass('highlight2');
		$("#mobile_error").html("�������ֻ�����");
		$("#mobile_error").removeClass().addClass("error");
		$("#mobile_error").show();
	}else if (validateRules.isNull(mobile) || !validateRules.isMobile(mobile)) {
        $("#mobile_error").html("�ֻ������ʽ������������ȷ���ֻ���");
        $("#mobile_error").removeClass().addClass("error");
        $("#mobile_error").removeClass().addClass("blank error-ico");
        $("#mobile_error").show();
        $('#mobile').removeClass().addClass('text highlight2');
        mobileFlag = false;
        return;
    }
    var mobileCode = $("#mobileCode").val();
	if (mobileCode == "") {
		$('#mobileCode').addClass('highlight2');
		$('#bmobileCode_error').removeClass().addClass('error').html('�����������֤��');
		$('#bmobileCode_error').show();
	} else {
		mobileCodeFlag = true;
	}
    var flag = validateFunction.emRegCompany_validate() && regnameOk && agreeProtocol && mobileCodeFlag;
    if (flag) {
        $("#registsubmit").attr({ "disabled": "disabled" }).removeClass().addClass("btn-img btn-regist wait-btn");
        $.ajax({
            type: "POST",
            url: "../reg/regService?r=" + Math.random(),
            contentType: "application/x-www-form-urlencoded; charset=utf-8",
            data: $("#formcompany").serialize(),
            success: function (result) {
                if (result) {
                    var obj = eval(result);
                    if (obj.info) {
                        $("#registsubmit").removeAttr("disabled").removeClass().addClass("btn-img btn-regist");
                        alert(obj.info);
                        verc();
                    }
                    if (obj.success == true) {
                        window.location = obj.dispatchUrl;
                    }
                }
            }

        });
    }
})
$(
    function () {
        refreshAreas(1, 0);
        function refreshAreas(level, parentId) {
            var myname;
            if (level == 1) {
                myname = "companycity";
                if (parentId == -1) {
                    $("#companycity").empty();
                    $("#companycity").append("<option value=\"-1\" selected>��ѡ��</option>");
                    $("#companycity").css({"width": "auto"});
                    $("#companyarea").empty();
                    $("#companyarea").append("<option value=\"-1\" selected>��ѡ��</option>");
                    $("#companyarea").css({"width": "auto"});
                }
            }
            else {
                myname = "companyarea";
                if (parentId == -1) {
                    $("#companyarea").empty();
                    $("#companyarea").append("<option value=\"-1\" selected>��ѡ��</option>");
                    $("#companyarea").css({"width": "auto"});
                }
            }
            if (parentId > 0) {
                $.getJSON(
                    "../reg/area?level=" + level + "&parentId=" + parentId + "&r=" + Math.random(),
                    function (result) {
                        if (result.Areas != null) {
                            $("#" + myname).empty();
                            $("#" + myname).append("<option value=\"-1\"  selected>��ѡ��</option>");
                            for (var i = 0; i < result.Areas.length; i++) {
                                var area = result.Areas[i];
                                $("#" + myname).append("<option  value=\"" + area.Id + "\">" + area.Name + "</option>");
                            }
                            $("#" + myname).css({"width": "Auto"});
                        }
                    });
            }
        }

        $("#companyprovince").change(
            function () {
                $("#hncompanyarea_error").removeClass();
                refreshAreas(1, parseInt($(this).val()));
                $("#companyarea").empty();
                $("#companyarea").append("<option value=\"-1\" selected>��ѡ��</option>");
            }
        )

        $("#companycity").change(
            function () {
                $("#hncompanyarea_error").removeClass();
                refreshAreas(2, parseInt($(this).val()));
            });
    })

function checkReadMe() {
    if ($("#readme").attr("checked") == true) {
        $("#protocol_error").removeClass().addClass("error hide");
        return true;
    } else {
        $("#protocol_error").removeClass().addClass("error");
        return false;
    }
}

function agreeonProtocol() {
    if ($("#readme").attr("checked") == true) {
        $("#protocol_error").removeClass().addClass("error hide");
        return true;
    }
}

