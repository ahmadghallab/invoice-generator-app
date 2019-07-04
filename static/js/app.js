function enterAsTab(formId, btnId) {
	$(formId).each(function () {
		$(this).find(':input').on("keydown", function (event) {
			if (event.keyCode == 13) {
				var isDisabled = $(btnId).is(':disabled');
				var inputs = $(this).parents(formId).find(":input:visible:not(:disabled):not([readonly])");
				var idx = inputs.index(this);
				if (!isDisabled) {
					$(btnId).click();
				} else if (idx == inputs.length - 1) {
					inputs[0].focus();
				} else {
					inputs[idx + 1].focus();
					// inputs[idx + 1].select();
				}
				return false;
			}
		});
	});
}
function validate(required_fields, btnId) {
	$(required_fields).on('keyup change', function () {
		let empty = false;
		$(required_fields).each(function () {
			if ($(this).val() == '') {
				empty = true
			}
		});
		if (empty) {
			$(btnId).attr('disabled', 'disabled');
		} else {
			$(btnId).removeAttr('disabled');
		}
	});
}
