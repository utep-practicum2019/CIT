//////////////////////////////////////
let TableLastSortedColumn = -1;

function SortTable() {
    let sortColumn = parseInt(arguments[0]);
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
    let table = document.getElementById(TableIDvalue);
    let tbody = table.getElementsByTagName("tbody")[0];
    let rows = tbody.getElementsByTagName("tr");
    let arrayOfRows = [];
    type = type.toUpperCase();
    dateformat.toLowerCase();
    for (let i = 0, len = rows.length; i < len; i++) {
        arrayOfRows[i] = {};
        arrayOfRows[i].oldIndex = i;
        let celltext = rows[i].getElementsByTagName("td")[sortColumn].innerHTML.replace(/<[^>]*>/g, "");
        if (type === 'D') {
            //arrayOfRows[i].value = GetDateSortingKey(dateformat, celltext);
        } else {
            let re = type === "N" ? /[^.\-+\d]/g : /[^a-zA-Z0-9]/g;
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
                arrayOfRows.sort(function (a, b) {
                    // Turn your strings into dates, and then subtract them
                    // to get a value that is either negative, positive, or zero.
                    return new Date(a) - new Date(b);
                });
                arrayOfRows.reverse();
                // arrayOfRows.sort(CompareRowOfNumbers);
                break;
            default  :
                arrayOfRows.sort(CompareRowOfText);
        }
    }

    let newTableBody = document.createElement("tbody");
    for (let i = 0, len = arrayOfRows.length; i < len; i++) {
        newTableBody.appendChild(rows[arrayOfRows[i].oldIndex].cloneNode(true));
    }
    table.replaceChild(newTableBody, tbody);
} // function SortTable()


/**
 * @return {number}
 */
function CompareRowOfText(a, b) {
    let aval = a.value;
    let bval = b.value;
    return (aval === bval ? 0 : (aval > bval ? 1 : -1));
} // function CompareRowOfText()

/**
 * @return {number}
 */
function CompareRowOfNumbers(a, b) {
    let aval = /\d/.test(a.value) ? parseFloat(a.value) : 0;
    let bval = /\d/.test(b.value) ? parseFloat(b.value) : 0;
    return (aval === bval ? 0 : (aval > bval ? 1 : -1));
} // function CompareRowOfNumbers()
// function GetDateSortingKey()