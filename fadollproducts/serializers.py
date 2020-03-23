from rest_framework import serializers
from .models import departments,categories,SubCategories,Attributes,AttributeValues,ProductNatures,CustomerClasses,Seasons,products,ProductImages,ProductAttributes,ProductAttributeValues,ProductReferences

class departmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = departments
        fields = ('id','DepartmentName','logo','description','active')

class categoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = categories
        fields = ('id','departments','CategoryName','logo','description','active')

class SubCategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategories
        fields = ('id','categories','SubCategoryName','logo','description','active')

class AttributesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attributes
        fields = ('id','AttributeName','description')

class AttributeValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AttributeValues
        fields = ('id','Attributes','AttributeValues','logo','description')

class ProductNaturesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductNatures
        fields = ('id','ProductNature','logo','description')

class CustomerClassesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerClasses
        fields = ('id','CustomerClass','logo','description','active')

class SeasonsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seasons
        fields = ('id','SeasonName','CalendarYear','CalendarDate','description','active')

class productsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = products
        fields = ('id','Seasons','SubCategories','ProductNatures','CustomerClasses','ProductName','description','ProductImage','ProductPrice','SalePrice','rating','caption','tag','active','CreateDBy','ModifiedBy','CreatedDate','ModifiedDate','ProductCode')

class ProductImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImages
        fields = ('id','products','SmallImage','LargeImage')

class ProductAttributesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = ('id','products','Attributes','active')

class ProductAttributeValuesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductAttributeValues
        fields = ('id','ProductAttributes','AttributeValues','active')

class ProductReferencesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductReferences
        fields = ('id','products','RefProductId')


