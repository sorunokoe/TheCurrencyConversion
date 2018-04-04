
angular.module("app", ['ngAnimate', 'ngRoute', 'ngCookies'])

.config(function($routeProvider, $httpProvider, $interpolateProvider, $qProvider){
	$interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

.controller("indexController",
function($scope, $http, $interval, $timeout, $cookies, $cookieStore, $rootScope, $window, $compile, $filter) {

    $scope.getCurrencies = function(){
        $http({
            url: '/api/currencies/',
            method: 'GET',
            contentType:'application/json'
         }).then(function successCallback(response) {
            //$cookies.putObject('currencies', response.data, {path: '/', secure: false});
            $scope.allcurrencies = response.data;
            $scope.allcurrencies.map(function(currency){
                if(currency.code=="USD"){
                    currency.choosed=true;
                    currency.enabled=true;
                    $scope.choosedCurrency = currency;
                }else{
                    currency.enabled=false;
                }
            });
            console.log($scope.allcurrencies);
         }, function errorCallback(response) {
            console.log(response);
         });
    }
    $scope.getCurrencies();

    $scope.choosed = function(currency){
        if(currency.enabled){
            $scope.allcurrencies.map(function(currency){
                currency.choosed=false;
            });
            currency.choosed=true;
            $scope.choosedCurrency = currency;
        }else{
            alert("API works for free of charge only for USD currency.")
        }
    }


    $scope.getRates = function(){
        $http({
            url: '/api/rates/',
            method: 'GET',
            contentType:'application/json'
         }).then(function successCallback(response) {
            //$cookies.putObject('currencies', response.data, {path: '/', secure: false});
            console.log(response.data);
            $scope.allrates = response.data;
         }, function errorCallback(response) {
            console.log(response);
         });
    }
    $scope.getRates();




    $scope.convert = function(){
        $scope.allrates.forEach(function(rates){
            if(rates.code == $scope.currency.targetCurrency){
                $scope.rate = rates;
            }
        });
        if($scope.rate){
            $scope.result = parseFloat($scope.currency.amount)*parseFloat($scope.rate.rate);
            $scope.sign = $scope.rate.code;
        }else{
            alert("Sorry, there is some problems..")
        }
    }


    $scope.changeTargetCurrency = function(){
        $scope.allrates.forEach(function(rates){
            if(rates.code == $scope.currency.targetCurrency){
                $scope.rate = rates;
            }
        });
        if($scope.rate){
            $scope.currency.rate = $scope.rate.rate;
            $scope.currency.sign = $scope.rate.code;
        }
    }




});
