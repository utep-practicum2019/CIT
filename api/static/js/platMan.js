(function load_platforms() {
    // noinspection JSUnusedGlobalSymbols
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/api/v2/resources/platform",
        contentType: "application/json",
        dataType: "json",
        data: {
            'all': 'True'
        },
        success: function (response) {
            //Print results
            console.log("Accessed Database at " + new Date().toUTCString());
            let array = response;
            let main_platforms_HTML = '<tbody>';
            for (let i in array) {
                // console.log(JSON.stringify(array[i]));
                let id = array[i]["main"]["id"];
                let name = array[i]["main"]["name"];
                let ip_port = array[i]["main"]["ip_port"];
                let note = array[i]["main"]["note"];
                let alias = array[i]["main"]["alias"];
                let date = array[i]["main"]["date_created"];
                // let fDate = new Date(date);
                // alert(fDate);
                main_platforms_HTML += '<tr><td style="text-align:center; vertical-align:middle;"><input aria-label="Checkbox for following text input" id="checkbox_platform'
                    + id + '" type="checkbox" name="checkbox_platform"></td>';
                main_platforms_HTML += `<td>${name}</td><td>${ip_port}</td><td>${id}</td>`;
                main_platforms_HTML +=
                    '<td>' +
                    '<form>' +
                    '<label>' +
                    '<input type="text" name="platformAliasBox" value="' + alias + '">' +
                    '</label>' +
                    '</form>' +
                    '</td>';
                main_platforms_HTML +=
                    '<td>' +
                    '<form>' +
                    '<label>' +
                    '<input type="text" name="platformNoteBox" value="' + note + '">' +
                    '</label>' +
                    '</form>' +
                    '</td>';
                main_platforms_HTML += `<td></td>`;
                main_platforms_HTML += `<td>${date}</td>`;
                main_platforms_HTML += '<td>\n' +
                    '<button onclick="load_subplatform_modal(' + id + ')" data-target="#subplatformModal" data-toggle="modal" id="subplatform' + id
                    + '" type="button">\n' +
                    'Subplatform\n' +
                    ' </button>\n' + '</td></tr>\'';
            }
            main_platforms_HTML += '</tbody>';
            $('#platformsTable tbody').replaceWith(main_platforms_HTML);
        },
        complete: function () {
            SortTable(7, 'D', 'platformsTable');
            // SortTable(7, 'D', 'platformsTable');
            load_platform_status();
        }
    });
})();

function check_all(table = "checkbox_platform") {
    let checkboxes = document.getElementsByName(table);
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = true;
    }
}

function uncheck_all(table = "checkbox_platform") {
    let checkboxes = document.getElementsByName(table);
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = false;
    }
}

function load_platform_status() {
    let list = [];
    $('#platformsTable input[type=checkbox]').each(function () {
        let data = $(this).parents('tr:eq(0)');
        list.push({
            'platform_ID': $(data).find('td:eq(3)').text()
        });
    });
    actionOnPlatforms(list, 0, "Status");
}

function reload_platforms() {
    // noinspection JSUnusedGlobalSymbols
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/api/v2/resources/platform",
        contentType: "application/json",
        dataType: "json",
        data: {
            'all': 'True'
        },
        success: function (response) {
            //Print results
            console.log("Accessed Database at " + new Date().toUTCString());
            let array = response;
            let main_platforms_HTML = '<tbody>';
            for (let i in array) {
                // console.log(JSON.stringify(array[i]));
                let id = array[i]["main"]["id"];
                let name = array[i]["main"]["name"];
                let ip_port = array[i]["main"]["ip_port"];
                let note = array[i]["main"]["note"];
                let alias = array[i]["main"]["alias"];
                let date = array[i]["main"]["date_created"];
                main_platforms_HTML += '<tr><td style="text-align:center; vertical-align:middle;"><input aria-label="Checkbox for following text input" id="checkbox_platform'
                    + id + '" type="checkbox" name="checkbox_platform"></td>';
                main_platforms_HTML += `<td>${name}</td><td>${ip_port}</td><td>${id}</td>`;
                main_platforms_HTML +=
                    '<td>' +
                    '<form>' +
                    '<label>' +
                    '<input type="text" name="platformAliasBox" value="' + alias + '">' +
                    '</label>' +
                    '</form>' +
                    '</td>';
                main_platforms_HTML +=
                    '<td>' +
                    '<form>' +
                    '<label>' +
                    '<input type="text" name="platformNoteBox" value="' + note + '">' +
                    '</label>' +
                    '</form>' +
                    '</td>';
                main_platforms_HTML += `<td></td>`;
                main_platforms_HTML += `<td>${date}</td>`;
                main_platforms_HTML += '<td>\n' +
                    '<button onclick="load_subplatform_modal(' + id + ')" data-target="#subplatformModal" data-toggle="modal" id="subplatform' + id
                    + '" type="button">\n' +
                    'Subplatform\n' +
                    ' </button>\n' + '</td></tr>\'';
            }
            main_platforms_HTML += '</tbody>';
            $('#platformsTable tbody').replaceWith(main_platforms_HTML);
        },
        complete: function () {
            SortTable(7, 'D', 'platformsTable');
            load_platform_status();
        }
    });
}

function load_subplatform_modal(id) {
    // noinspection JSUnusedGlobalSymbols
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/api/v2/resources/platform",
        contentType: "application/json",
        dataType: "json",
        data: {
            'platform_ID': id,
            'sub': 'true',
            'status': 'true'
        },
        success: function (response) {
            //Print results
            console.log("Accessed Database at " + new Date().toUTCString());
            let array = response["subplatforms"];
            let trHTML = '<tbody>';
            for (let i in array) {
                // console.log(JSON.stringify(array[i]));
                let id = array[i]["id"];
                let name = array[i]["name"];
                let ip_port = array[i]["ip_port"];
                let status = array[i]["status"] ? "Running" : "Stopped";
                let date = response["main"]["date_created"];
                trHTML += `<tr><td>${name}</td><td>${ip_port}</td><td>${id}</td><td>${status}</td><td>${date}</td>`;
                // if (id === array[i]["main"]["id"]) {
                //     let subplats = array[i]["subplatforms"];
                //     for (let j in subplats) {
                //         let id = array[i]["subplatforms"][j]["id"];
                //         let name = array[i]["subplatforms"][j]["name"];
                //         let ip_port = array[i]["subplatforms"][j]["ip_port"];
                //         let alias = array[i]["main"]["alias"];
                //         let date = array[i]["main"]["date_created"];
                //         trHTML += `<tr><td>${name}</td><td>${ip_port}</td><td>${id}</td><td>${alias}</td><td>${date}</td>`;
                //     }
                // }
            }
            trHTML += '</tr></tbody>';
            $('#subplatformstable > tbody').replaceWith(trHTML);
            // SortTable(0, 'T', 'platformsTable', true)
        }
    });
}

// function select_platforms() {
//     // var values = [];
//     // $.each($("input[type=checkbox]:checked"), function () {
//     //     var data = $(this).parents('tr:eq(0)');
//     //     values.push({
//     //         'callphone': $(data).find('td:eq(1)').text(),
//     //         'rating': $(data).find('td:eq(2)').text(),
//     //         'location': $(data).find('td:eq(3)').text()
//     //     });
//     // });
//     // alert(JSON.stringify(values));
//     let values = [];
//     $.each($("input[type=checkbox]:checked"), function () {
//         let data = $(this).parents('tr:eq(0)');
//         values.push({
//             'platform_ID': $(data).find('td:eq(3)').text()
//         });
//     });
//     return values;
// }

function select_platforms() {
    let list = [];
    $('#platformsTable input[type=checkbox]:checked').each(function () {
        let data = $(this).parents('tr:eq(0)');
        list.push({
            'platform_ID': $(data).find('td:eq(3)').text()
        });
    });
    return list;
}


// Get Plugin List for Platform Creation
$(document).ready(function () {
    $('#createNewPlatBtn').click(function () {
        $.ajax({
            type: "GET",
            url: "http://localhost:5001/api/v2/resources/platform",
            contentType: "application/json",
            dataType: "json",
            data: {
                'all': 'False'
            },
            success: function (response) {
                console.log("Accessed Database at " + new Date().toUTCString());
                let main_plats = response["main_platforms"];
                let sub_plats = response["sub_platforms"];
                let mainPlatRadio = '';
                let subPlatCheck = '';
                for (let i in main_plats) {
                    mainPlatRadio += `<input name="mainPlat" type="radio" value="${main_plats[i]}"> ${main_plats[i]}<br>`;
                }
                for (let i in sub_plats) {
                    subPlatCheck += `<input name="subPlat" type="checkbox" value="${sub_plats[i]}"> ${sub_plats[i]}<br>`;
                }
                $('#mainPlatRadio').replaceWith(mainPlatRadio);
                $('#subPlatCheck').replaceWith(subPlatCheck);
            }
        });
    });
});

// Create Platform
$(document).ready(function () {
    $('#btnCreatePlatform').click(function () {
        let mainPlat = $("input[name='mainPlat']:checked").val();
        if (mainPlat == null) {
            $.notify("Must select a main platform!", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
            return;
        }
        let subplats = [];
        let errors = false;
        $.each($("input[name='subPlat']:checked"), function () {
            if ($(this).val() === mainPlat) {
                errors = true;
            }
            subplats.push($(this).val());
        });
        if (errors) {
            $.notify("Main Platform and Subplatform cannot be equal!", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
            return;
        }
        let request = {
            "main_platform": mainPlat,
            "subplatforms": subplats
        };
        $.ajax({
            type: "POST",
            url: "http://localhost:5001/api/v2/resources/platform",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(request),
            success: function (response) {
                console.log(JSON.stringify(response));
                if (response["Status"] === "Success") {
                    $.notify("Platform Added Successfully!", {
                        type: 'success',
                        animate: {
                            enter: 'animated fadeInRight',
                            exit: 'animated fadeOutRight'
                        },
                        offset: 20,
                        spacing: 10,
                        newest_on_top: true
                    });
                } else {
                    $.notify("Couldn't create platform!", {
                        type: 'danger',
                        animate: {
                            enter: 'animated fadeInRight',
                            exit: 'animated fadeOutRight'
                        },
                        offset: 20,
                        spacing: 10,
                        newest_on_top: true
                    });
                }
            },
            complete: function () {
                reload_platforms();
                load_platform_status();
            }
        });
    })
});

// // Start Platform
// $(document).ready(function () {
//     $('#btnStart').click(function () {
//         let list_of_platforms = select_platforms();
//         if (list_of_platforms.length === 0) {
//             alert("Please select at least one platform to start.");
//         } else {
//             actionOnPlatforms(list_of_platforms, 0, "Start");
//             alert("Platforms Started!");
//         }
//     });
// });

// function isSiteOnline(url, callback) {
//     // try to load favicon
//     let timer = setTimeout(function () {
//         // timeout after 5 seconds
//         callback(false);
//     }, 5000);
//     let img = document.createElement("img");
//     img.onload = function () {
//         clearTimeout(timer);
//         callback(true);
//     };
//     img.onerror = function () {
//         clearTimeout(timer);
//         callback(false);
//     };
//     img.src = url + "/favicon.ico";
// }

let wait = ms => new Promise((r) => setTimeout(r, ms));

// async function is_rocket_chat_online() {
//     let counter = 0;
//     while (counter < 20) {
//         let rocket_on = await new Promise((resolve) =>
//             isSiteOnline("http://0.0.0.0:3000", function (found) {
//                 if (found) {
//                     console.log("Rocket Chat Is Up");
//                     resolve(true);
//                 } else {
//                     console.log("Rocket Chat Is Down");
//                     resolve(false);
//                 }
//             }));
//         if (rocket_on) {
//             return Promise.resolve(true);
//         }
//         await wait(1000);
//         counter++;
//     }
//     return Promise.resolve(false);
// }

// async function is_tiddly_wiki_online() {
//     let counter = 0;
//     while (counter < 20) {
//         let tiddly_on = await new Promise((resolve) =>
//             isSiteOnline("http://129.108.7.29:8085", function (found) {
//                 if (found) {
//                     console.log("Tiddly Wiki Is Up");
//                     resolve(true);
//                 } else {
//                     console.log("Tiddly Wiki Is Down");
//                     resolve(false);
//                 }
//             }));
//         if (tiddly_on) {
//             return Promise.resolve(true);
//         }
//         await wait(1000);
//         counter++;
//     }
//     return Promise.resolve(false);
// }

function start_platform() {
    let list_of_platforms = select_platforms();
    if (list_of_platforms.length === 0) {
        $.notify("Please select at least one platform to start.", {
            type: 'danger',
            animate: {
                enter: 'animated fadeInRight',
                exit: 'animated fadeOutRight'
            },
            offset: 20,
            spacing: 10,
            newest_on_top: true
        });
    } else {
        $.notify(list_of_platforms.length + " platform(s) are being started!", {
            type: 'info',
            animate: {
                enter: 'animated fadeInRight',
                exit: 'animated fadeOutRight'
            },
            offset: 20,
            spacing: 10,
            newest_on_top: true
        });
        $("#start_spinner").css("display", "inline-block");
        actionOnPlatforms(list_of_platforms, 0, "Start");
    }
}

// async function get_subplatforms(list_of_platforms) {
//     let subplats = await new Promise((resolve) =>
//         $.ajax({
//             type: "GET",
//             url: "http://localhost:5001/api/v2/resources/platform",
//             contentType: "application/json",
//             dataType: "json",
//             data: {
//                 'all': 'True'
//             },
//             success: function (response) {
//                 //Print results
//                 console.log("Accessed Database at " + new Date().toUTCString());
//                 let array = response;
//                 let to_return = [];
//                 for (let plat in list_of_platforms) {
//                     for (let i in array) {
//                         if (parseInt(list_of_platforms[plat]["platform_ID"]) === array[i]["main"]["id"]) {
//                             let subplats = array[i]["subplatforms"];
//                             let to_insert = [];
//                             for (let j in subplats) {
//                                 to_insert.push(array[i]["subplatforms"][j]["name"]);
//                             }
//                             to_return.push(to_insert);
//                         }
//                     }
//                 }
//                 resolve(to_return);
//             }
//         }));
//     return Promise.resolve(subplats);
// }

// $('#platformStartLoadModal').on('shown.bs.modal', function () {
//     let list_of_platforms = select_platforms();
//     let subplats = get_subplatforms(list_of_platforms);
//     subplats.then(function (subplatforms) {
//         for (let plat in subplatforms) {
//             if (subplatforms[plat].includes("Rocketchat")) {
//                 let rocket_status = is_rocket_chat_online();
//                 rocket_status.then(function (rocket_online) {
//                     if (rocket_online) {
//                         $.notify("Platforms Sucesfully Started!", {
//                             type: 'success',
//                             animate: {
//                                 enter: 'animated fadeInRight',
//                                 exit: 'animated fadeOutRight'
//                             },
//                             offset: 20,
//                             spacing: 10,
//                             newest_on_top: true
//                         });
//                     } else {
//                         $.notify("Couldn't Start Platforms!", {
//                             type: 'danger',
//                             animate: {
//                                 enter: 'animated fadeInRight',
//                                 exit: 'animated fadeOutRight'
//                             },
//                             offset: 20,
//                             spacing: 10,
//                             newest_on_top: true
//                         });
//                     }
//                     $('#platformStartLoadModal').modal('hide');
//                 });
//             }
//             <!--                else if (subplatforms[plat].includes("TiddlyWiki")){-->
//             <!--                    let tiddly_status = is_tiddly_wiki_online();-->
//             <!--                    tiddly_status.then(function (tiddly_online) {-->
//             <!--                        if (tiddly_online) {-->
//             <!--                            alert("Platforms Sucesfully Started!");-->
//             <!--                        } else {-->
//             <!--                            alert("Couldn't Start Platforms!");-->
//             <!--                        }-->
//             <!--                        $('#platformStartLoadModal').modal('hide');-->
//             <!--                    });-->
//             <!--                }-->
//             else {
//                 $('#platformStartLoadModal').modal('hide');
//             }
//         }
//     });
//     actionOnPlatforms(list_of_platforms, 0, "Status");
// });

// Stop Platform
$(document).ready(function () {
    $('#btnStop').click(function () {
        let list_of_platforms = select_platforms();
        if (list_of_platforms.length === 0) {
            $.notify("Please select at least one platform to stop.", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        } else {
            actionOnPlatforms(list_of_platforms, 0, "Stop");
            $.notify("Platforms Stopped!", {
                type: 'success',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        }
    });
});

// Delete platforms
$(document).ready(function () {
    $('#btnDelPlat').click(function () {
        let list_of_platforms = select_platforms();
        if (list_of_platforms.length === 0) {
            $.notify("Please select at least one platform for deletion.", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        } else {
            $.notify(list_of_platforms.length + " platform(s) are being deleted!", {
                type: 'info',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
            $("#delete_spinner").css("display", "inline-block");
            actionOnPlatforms(list_of_platforms, 0, "Delete");
        }
    });
});

function actionOnPlatforms(platforms, index, action, wait = 0) {
    if (index < platforms.length) {
        switch (action) {
            case "Delete":
                $.ajax({
                    type: "DELETE",
                    url: "http://0.0.0.0:5001/api/v2/resources/platform",
                    contentType: "application/json",
                    dataType: "json",
                    data: JSON.stringify({
                        "platform_ID": platforms[index]["platform_ID"],
                        "subplatforms_IDS": []
                    }),
                    statusCode: {
                        500: function () {
                            $.notify("Could not delete platform " + platforms[index]["platform_ID"], {
                                type: 'danger',
                                animate: {
                                    enter: 'animated fadeInRight',
                                    exit: 'animated fadeOutRight'
                                },
                                offset: 20,
                                spacing: 10,
                                newest_on_top: true
                            });
                        }
                    },
                    success: function (response) {
                        console.log(JSON.stringify(response));
                    },
                    complete: function () {
                        actionOnPlatforms(platforms, index + 1, action)
                    }
                });
                break;
            case "Start":
                $.ajax({
                    type: "PUT",
                    url: "http://0.0.0.0:5001/api/v2/resources/platform",
                    contentType: "application/json",
                    dataType: "json",
                    data: JSON.stringify({
                        "command": "start",
                        "platform_ID": platforms[index]["platform_ID"],
                        "subplatforms_IDS": []
                    }),
                    statusCode: {
                        500: function () {
                            $.notify("Could not start platform " + platforms[index]["platform_ID"], {
                                type: 'danger',
                                animate: {
                                    enter: 'animated fadeInRight',
                                    exit: 'animated fadeOutRight'
                                },
                                offset: 20,
                                spacing: 10,
                                newest_on_top: true
                            });
                        }
                    },
                    success: function (response) {
                        console.log(JSON.stringify(response));
                        let plat_status = response["Status"];
                        if (plat_status === "Success") {
                            $.notify("Succesfully started platform " + platforms[index]["platform_ID"], {
                                type: 'success',
                                animate: {
                                    enter: 'animated fadeInRight',
                                    exit: 'animated fadeOutRight'
                                },
                                offset: 20,
                                spacing: 10,
                                newest_on_top: true
                            });
                        } else {
                            $.notify("There were issues starting platform " + platforms[index]["platform_ID"], {
                                type: 'danger',
                                animate: {
                                    enter: 'animated fadeInRight',
                                    exit: 'animated fadeOutRight'
                                },
                                offset: 20,
                                spacing: 10,
                                newest_on_top: true
                            });
                        }
                    },
                    complete: function () {
                        actionOnPlatforms(platforms, index + 1, action)
                    }
                });
                break;
            case "Stop":
                $.ajax({
                    type: "PUT",
                    url: "http://0.0.0.0:5001/api/v2/resources/platform",
                    contentType: "application/json",
                    dataType: "json",
                    data: JSON.stringify({
                        "command": "stop",
                        "platform_ID": platforms[index]["platform_ID"],
                        "subplatforms_IDS": []
                    }),
                    statusCode: {
                        500: function () {
                            $.notify("Could not stop platform " + platforms[index]["platform_ID"], {
                                type: 'danger',
                                animate: {
                                    enter: 'animated fadeInRight',
                                    exit: 'animated fadeOutRight'
                                },
                                offset: 20,
                                spacing: 10,
                                newest_on_top: true
                            });
                        }
                    },
                    success: function (response) {
                        console.log(JSON.stringify(response));
                    },
                    complete: function () {
                        actionOnPlatforms(platforms, index + 1, action)
                    }
                });
                break;
            case "Status":
                $.ajax({
                    type: "GET",
                    url: "http://localhost:5001/api/v2/resources/platform",
                    contentType: "application/json",
                    dataType: "json",
                    data: {
                        'status': 'True',
                        'platform_ID': platforms[index]["platform_ID"],
                        'wait': wait
                    },
                    success: function (response) {
                        let status = response;
                        console.log(response);
                        $('#platformsTable > tbody ').find('tr:eq(' + index + ')').find('td:eq(6)').replaceWith(`<td>${status}</td>`);
                    },
                    complete: function () {
                        actionOnPlatforms(platforms, index + 1, action)
                    }
                });
                break;
        }
    } else {
        switch (action) {
            case "Delete":
                reload_platforms();
                $.notify("Completed delete command", {
                    type: 'success',
                    animate: {
                        enter: 'animated fadeInRight',
                        exit: 'animated fadeOutRight'
                    },
                    offset: 20,
                    spacing: 10,
                    newest_on_top: true
                });
                $("#delete_spinner").css("display", "none");
                break;
            case "Start":
                $.notify("Completed start command, platform status will be updated shortly", {
                    type: 'success',
                    animate: {
                        enter: 'animated fadeInRight',
                        exit: 'animated fadeOutRight'
                    },
                    offset: 20,
                    spacing: 10,
                    newest_on_top: true
                });
                actionOnPlatforms(platforms, 0, "Status", 4);
                break;
            case "Stop":
                $.notify("Completed stop command", {
                    type: 'success',
                    animate: {
                        enter: 'animated fadeInRight',
                        exit: 'animated fadeOutRight'
                    },
                    offset: 20,
                    spacing: 10,
                    newest_on_top: true
                });
                actionOnPlatforms(platforms, 0, "Status");
                break;
            case "Status":
                $("#start_spinner").css("display", "none");
                break;
        }
    }
}

// Save Platform Notes
$(document).ready(function () {
    $('#savePlatformNotesBtn').click(function () {
        let platforms = selectPlatformObjectsCheck();
        if (platforms.length < 1) {
            $.notify("At least one platform must be selected!", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        } else {
            addToPlatform(platforms, 0, "Note");
            $.notify("Platform Notes saved.", {
                type: 'success',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        }
    });
});

// Save Platform Aliases
$(document).ready(function () {
    $('#savePlatformAliasBtn').click(function () {
        let platforms = selectPlatformObjectsCheck();
        if (platforms.length < 1) {
            $.notify("At least one platform must be selected!!", {
                type: 'danger',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        } else {
            addToPlatform(platforms, 0, "Alias");
            $.notify("Platform Aliases saved.", {
                type: 'success',
                animate: {
                    enter: 'animated fadeInRight',
                    exit: 'animated fadeOutRight'
                },
                offset: 20,
                spacing: 10,
                newest_on_top: true
            });
        }
    });
});

// Clear Platform Notes
$(document).ready(function () {
    $('#clearPlatformNotesBtn').click(function () {
        $.each($("input[type=checkbox]:checked"), function () {
            let data = $(this).parents('tr:eq(0)');
            $(data).find('td:eq(5)').find('input[name="platformNoteBox"]').val("");
        });
        // $('#platformsTable > tbody > tr').each(function () {
        //     $(this).find('td:eq(5)').find('input[name="platformNoteBox"]').val("");
        // });
    });
});

// Clear Platform Aliases
$(document).ready(function () {
    $('#clearPlatformAliasBtn').click(function () {
        $.each($("input[type=checkbox]:checked"), function () {
            let data = $(this).parents('tr:eq(0)');
            $(data).find('td:eq(4)').find('input[name="platformAliasBox"]').val("");
        });
        // $('#platformsTable > tbody > tr').each(function () {
        //     $(this).find('td:eq(4)').find('input[name="platformAliasBox"]').val("");
        // });
    });
});

$('.modal-content').resizable({
    //alsoResize: ".modal-dialog",
    minHeight: 300,
    minWidth: 300
});

// noinspection JSValidateTypes
$(".modal-dialog").draggable({
    handle: ".modal-header"
});

$('#subplatformModal').on('shown.bs.modal', function () {
    $(this).find('.modal-dialog').css({
        width: 'auto', //probably not needed
        height: 'auto', //probably not needed
        'max-height': '100%'
    });
});


// Create a list of group objects from the table
function selectPlatformObjectsCheck() {
    let platforms = [];
    $.each($("input[type=checkbox]:checked"), function () {
        let data = $(this).parents('tr:eq(0)');
        platforms.push({
            'name': $(data).find('td:eq(1)').text(),
            'ip_port': $(data).find('td:eq(2)').text(),
            'id': $(data).find('td:eq(3)').text(),
            'alias': $(data).find('td:eq(4)').find('input[name="platformAliasBox"]').val(),
            'note': $(data).find('td:eq(5)').find('input[name="platformNoteBox"]').val()
        });
    });
    return platforms;
}

// Add users
function addToPlatform(platforms, index, to_add) {
    if (index < platforms.length) {
        let platform_ID = platforms[index]["id"];
        let platform_object = {
            "platform_ID": platform_ID,
        };
        switch (to_add) {
            case "Note":
                platform_object["note"] = platforms[index]["note"];
                break;
            case "Alias":
                platform_object["alias"] = platforms[index]["alias"];
                break;
        }
        $.ajax({
            type: "PUT",
            url: "http://0.0.0.0:5001/api/v2/resources/platform",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify(platform_object),
            success: function (response) {
                console.log(JSON.stringify(response));
            },
            complete: function () {
                addToPlatform(platforms, index + 1, to_add);
            }
        });
    } else {
        switch (to_add) {
            case "Note":
                reload_platform_notes();
                break;
            case "Alias":
                reload_platform_aliases();
                break;
        }
    }
}

function reload_platform_notes() {
    // noinspection JSUnusedGlobalSymbols
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/api/v2/resources/platform",
        contentType: "application/json",
        dataType: "json",
        data: {
            'all': 'True'
        },
        success: function (response) {
            //Print results
            console.log("Accessed Database at " + new Date().toUTCString());
            let array = response;
            for (let i in array) {
                let note = array[i]["main"]["note"];
                $('#platformsTable > tbody').each(function () {
                    $(this).find('tr:eq(' + i + ')').find('td:eq(5)').find('input[name="platformNoteBox"]').val(note);
                });
            }
        }
    });
}

function reload_platform_aliases() {
    // noinspection JSUnusedGlobalSymbols
    $.ajax({
        type: "GET",
        url: "http://localhost:5001/api/v2/resources/platform",
        contentType: "application/json",
        dataType: "json",
        data: {
            'all': 'True'
        },
        success: function (response) {
            //Print results
            console.log("Accessed Database at " + new Date().toUTCString());
            let array = response;
            for (let i in array) {
                let alias = array[i]["main"]["alias"];
                $('#platformsTable > tbody').each(function () {
                    $(this).find('tr:eq(' + i + ')').find('td:eq(4)').find('input[name="platformAliasBox"]').val(alias);
                });
            }
        }
    });
}

// function reload_platform_status(row_number, platform_id) {
//     $.ajax({
//         type: "GET",
//         url: "http://localhost:5001/api/v2/resources/platform",
//         contentType: "application/json",
//         dataType: "json",
//         data: {
//             'status': 'True',
//             'platform_ID': platform_id
//         },
//         success: function (response) {
//             let status = "Stopped!";
//             if (response === true) {
//                 status = "Running!"
//             }
//             console.log("HHHHH:" + response);
//             $('#platformsTable > tbody').find('tr:eq(' + row_number + ')').find('td:eq(6)').text(status);
//         }
//     });
// }
