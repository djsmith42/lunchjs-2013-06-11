angular.module("MyApp", []).
controller("MyController", function($scope) {
    $scope.imageToShow = 1;

    $scope.showImage = function(number) {
        $scope.imageToShow = number;
    }
})
