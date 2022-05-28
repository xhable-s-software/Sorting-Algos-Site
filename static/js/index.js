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
  $(function () {
    $("table.sortable")
      .tablesort()
      .data("tablesort")
      .sort($("th.default-sort"));
  });

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
  $(".ui.dropdown").dropdown();
  $("table").tablesort();

  // Обновление таблицы с помощью AJAX
  $(".selection").change(function () {
    var sort_percentage = document.getElementById("select_sort_percentage");
    var item_count = document.getElementById("select_item_count");

    $.ajax({
      data: 0,
      url: "ajax/algos/" + item_count.value + "/" + sort_percentage.value,
      success: function (response) {
        $("tbody").replaceWith(response.table);
      },
      error: function (response) {
        console.log(response.responseJSON.errors);
        alert(response.responseJSON.errors);
      },
    }).then(function () {
      $("table.sortable")
        .tablesort()
        .data("tablesort")
        .sort($("th.default-sort"));
    });

    return false;
  });
};
