$(document).ready(function () {
  // fixed menu when passed
  $(".masthead").visibility({
    once: false,
    onBottomPassed: function () {
      $(".fixed.menu").transition("fade in");
    },
    onBottomPassedReverse: function () {
      $(".fixed.menu").transition("fade out");
    },
  });

  // create sidebar and attach to menu open
  $(".ui.sidebar").sidebar("attach events", ".toc.item");
});

$(document).ready(function () {
  $(".algo_name_link").click(function () {
    $.ajax({
      data: 0,
      url: "ajax/algos_code/" + $(this).attr("algo_name"),
      success: function (response) {
        $("#modal-content").replaceWith(response.modal_content);
      },
      error: function (response) {
        console.log(response.responseJSON.errors);
        alert(response.responseJSON.errors);
      },
    });
    console.log("highlighted!");
    $(".ui.modal").modal("show");
    hljs.highlightAll();
    return false;
  });
});

$(document).ready(function ScrollTo() {
  $("a").click(function () {
    $("html, body").animate(
      {
        scrollTop: $($.attr(this, "href")).offset().top,
      },
      500
    );
    return false;
  });
});

window.onload = function () {
  // hljs.initHighlightingOnLoad();
  $("table").tablesort(); // Make the table sortable.
  // var tablesort = $("table").data("tablesort"); // Get a reference to it's tablesort instance
  // $("div[data-gist]").ajaxgist();

  // Обновление таблицы с помощью AJAX
  $(".selection").change(function () {
    // alert(this.value);

    $.ajax({
      data: 0,
      url:
        "ajax/algos/" +
        document.getElementsByClassName("selection")[1].value +
        "/" +
        document.getElementsByClassName("selection")[0].value,
      success: function (response) {
        $("tbody").replaceWith(response.table);
      },
      error: function (response) {
        console.log(response.responseJSON.errors);
        alert(response.responseJSON.errors);
      },
    });

    $(function () {
      $("table.sortable").tablesort().data("tablesort").sort($("th"));
    });

    return false;
  });
};
