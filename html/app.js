
var API_base = "HashReversing/JSON";
var hash_types = ["MD5", "SHA1", "SHA256", "SHA512"];
var info_pages = ["About", "API", "Contacts"];


function GetCurrentHashType(route)
{
	var current_hash_type = hash_types[0];
	for (var idx in hash_types)
	{
		if (route.current.templateUrl.indexOf(hash_types[idx]) !== -1)
		{
			current_hash_type = hash_types[idx];
			break;
		}
	}
	return current_hash_type;
}


var app = angular.module('HashReversing', ["ngRoute"]);
app.controller('HashReversingController', function($scope, $timeout, $http, $route) {
	$scope.hash_types = hash_types;
	$scope.info_pages = info_pages
	$scope.inputs = {};
	$scope.inputs.hash_error = null;
	$scope.inputs.value_error = null;
	$scope.inputs.value_warning = null;
	$scope.inputs.registration_status = null;

	$scope.$on('$routeChangeStart', function($event, next, current) {
		delete $scope.inputs.hash;
		delete $scope.inputs.value;
		$scope.inputs.hash_error = null;
		$scope.inputs.value_error = null;
		$scope.inputs.value_warning = null;
		$scope.inputs.registration_status = null;
	});

	$scope.on_value_change = function(new_value) {
		if (typeof $scope.update_delayer != "undefined")
			$timeout.cancel($scope.update_delayer);

		if (new_value.length == 0)
			return;

		var current_hash_type = GetCurrentHashType($route);

		$scope.update_delayer = $timeout(function() {
			$http.get(API_base + "/" + current_hash_type + "/digest", {
				params: {value: new_value}
			}).then(function(response) {
				delete $scope.inputs.value_error;
				delete $scope.inputs.hash_error;
				delete $scope.inputs.value_warning;
				$scope.inputs.hash = response.data.digest;
				$scope.inputs.registration_status = null;
			},
			function (response) {
				delete $scope.inputs.hash;
				delete $scope.inputs.value_warning;
				$scope.inputs.registration_status = null;
				$scope.inputs.value_error = response.data.error;
			}
			)}, 500);
	}

	$scope.on_hash_change = function(new_hash) {
		if (typeof $scope.update_delayer != "undefined")
			$timeout.cancel($scope.update_delayer);

		if (new_hash.length == 0)
			return;

		var current_hash_type = GetCurrentHashType($route);

		$scope.update_delayer = $timeout(function() {
			$http.get(API_base + "/" + current_hash_type + "/value", {
				params: {digest: new_hash}
			}).then(function(response) {
				delete $scope.inputs.value_error;
				delete $scope.inputs.hash_error;
				delete $scope.inputs.value_warning;

				if (response.data.value == null)
				{
					$scope.inputs.value_warning = "Value not found";
					$scope.inputs.value = "Value not found for specified hash";
					$scope.inputs.registration_status = null;
				}
				else
				{
					$scope.inputs.value = response.data.value;
					$scope.inputs.registration_status = null;
				}

			},
			function (response) {
				delete $scope.inputs.value;
				delete $scope.inputs.value_warning;
				$scope.inputs.hash_error = response.data.error;
				$scope.inputs.registration_status = null;
			}
			)}, 500);

	}

	$scope.register_notify = function(email) {
		var current_hash_type = GetCurrentHashType($route);
		$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
		$http.post(API_base + "/" + current_hash_type + "/notification",
				"email=" + escape($scope.inputs.notify_email) +
				"&algorithm=" + escape(current_hash_type) +
				"&digest=" + escape($scope.inputs.hash)).then(function(response) {
			$scope.inputs.registration_status = "ok";
		});
	}
});

app.config(function ($routeProvider) {

	$routeProvider.when("/", {
		templateUrl : hash_types[0] + ".html"
	});

	for (var idx in hash_types)
	{
		requested_URL = "/" + hash_types[idx];
		required_URL = requested_URL + ".html";
		$routeProvider.when(requested_URL, {
			templateUrl : required_URL
		});
	}

	for (var idx in info_pages)
	{
		requested_URL = "/" + info_pages[idx];
		required_URL = requested_URL + ".html";
		$routeProvider.when(requested_URL, {
			templateUrl : required_URL
		});
	}

	$routeProvider.otherwise({
		template : "<p>Unknown page requested</p>"
	});
});


