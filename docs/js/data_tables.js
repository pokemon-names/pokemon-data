var DataTables = DataTables || {};

DataTables = {
    init: function (options) {
        options = options || {};
        var uri = options.uri || false;

        // Fetch the source data
        $.get({
              url: uri,
              data: {},
              success: null,
              dataType: 'json'
        });

        // Save to a file
    }
};
