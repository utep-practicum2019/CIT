//////////////////////////////////////
let TableLastSortedColumn = -1;

function SortTable() {
    var sortColumn = parseInt(arguments[0]);
    let type = arguments.length > 1 ? arguments[1] : 'T';
    let dateformat = '';
    let TableIDvalue;
    let resort = false;
    // if (type === 'D') {
    //     dateformat = arguments.length > 2 ? arguments[2] : '';
    //     TableIDvalue = arguments[3];
    //     if (arguments.length === 5) {
    //         resort = arguments[4];
    //     }
    // } else {
        TableIDvalue = arguments[2];
        if (arguments.length === 4) {
            resort = arguments[3];
        }
    // }
    var table = document.getElementById(TableIDvalue);
    var tbody = table.getElementsByTagName("tbody")[0];
    var rows = tbody.getElementsByTagName("tr");
    var arrayOfRows = [];
    type = type.toUpperCase();
    dateformat = dateformat.toLowerCase();
    for (var i = 0, len = rows.length; i < len; i++) {
        arrayOfRows[i] = {};
        arrayOfRows[i].oldIndex = i;
        var celltext = rows[i].getElementsByTagName("td")[sortColumn].innerHTML.replace(/<[^>]*>/g, "");
        if (type === 'D') {
            //arrayOfRows[i].value = GetDateSortingKey(dateformat, celltext);
        } else {
            var re = type === "N" ? /[^.\-+\d]/g : /[^a-zA-Z0-9]/g;
            arrayOfRows[i].value = celltext.replace(re, "").substr(0, 25).toLowerCase();
        }
    }

    if (sortColumn === TableLastSortedColumn && !resort) {
        arrayOfRows.reverse();
    } else {
        TableLastSortedColumn = sortColumn;


        switch (type) {
            case "N" :
                arrayOfRows.sort(CompareRowOfNumbers);
                break;
            case "D" :
                arrayOfRows.sort(function(a,b){
                    // Turn your strings into dates, and then subtract them
                    // to get a value that is either negative, positive, or zero.
                    return new Date(a) - new Date(b);
                });
                // arrayOfRows.sort(CompareRowOfNumbers);
                break;
            default  :
                arrayOfRows.sort(CompareRowOfText);
        }


    }

    var newTableBody = document.createElement("tbody");
    for (var i = 0, len = arrayOfRows.length; i < len; i++) {
        newTableBody.appendChild(rows[arrayOfRows[i].oldIndex].cloneNode(true));
    }
    table.replaceChild(newTableBody, tbody);
} // function SortTable()


/**
 * @return {number}
 */
function CompareRowOfText(a, b) {
    var aval = a.value;
    var bval = b.value;
    return (aval === bval ? 0 : (aval > bval ? 1 : -1));
} // function CompareRowOfText()

/**
 * @return {number}
 */
function CompareRowOfNumbers(a, b) {
    var aval = /\d/.test(a.value) ? parseFloat(a.value) : 0;
    var bval = /\d/.test(b.value) ? parseFloat(b.value) : 0;
    return (aval == bval ? 0 : (aval > bval ? 1 : -1));
} // function CompareRowOfNumbers()




/**
 * @return {string}
 */
function GetDateSortingKey(format, text) {
    if (format.length < 1) {
        return "";
    }
    format = format.toLowerCase();
    text = text.toLowerCase();
    text = text.replace(/^[^a-z0-9]*/, "");
    text = text.replace(/[^a-z0-9]*$/, "");
    if (text.length < 1) {
        return "";
    }
    text = text.replace(/[^a-z0-9]+/g, ",");
    var date = text.split(",");
    if (date.length < 3) {
        return "";
    }
    var d = 0, m = 0, y = 0;
    for (var i = 0; i < 3; i++) {
        var ts = format.substr(i, 1);
        if (ts === "d") {
            d = date[i];
        } else if (ts === "m") {
            m = date[i];
        } else if (ts === "y") {
            y = date[i];
        }
    }
    d = d.replace(/^0/, "");
    if (d < 10) {
        d = "0" + d;
    }
    if (/[a-z]/.test(m)) {
        m = m.substr(0, 3);
        switch (m) {
            case "jan" :
                m = String(1);
                break;
            case "feb" :
                m = String(2);
                break;
            case "mar" :
                m = String(3);
                break;
            case "apr" :
                m = String(4);
                break;
            case "may" :
                m = String(5);
                break;
            case "jun" :
                m = String(6);
                break;
            case "jul" :
                m = String(7);
                break;
            case "aug" :
                m = String(8);
                break;
            case "sep" :
                m = String(9);
                break;
            case "oct" :
                m = String(10);
                break;
            case "nov" :
                m = String(11);
                break;
            case "dec" :
                m = String(12);
                break;
            default    :
                m = String(0);
        }
    }
    m = m.replace(/^0/, "");
    if (m < 10) {
        m = "0" + m;
    }
    y = parseInt(y);
    if (y < 100) {
        y = parseInt(y) + 2000;
    }
    return "" + String(y) + "" + String(m) + "" + String(d) + "";
} // function GetDateSortingKey()