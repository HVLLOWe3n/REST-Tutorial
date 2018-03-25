from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    """
    Класс определяет поля, которые становятся сериализованными / десериализованными.
    """
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        Создает и возвращает новый экземпляр «Snippet», учитывая проверенные данные
        :param validated_data:
        :return:
        """

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Обновляет и возвращает существующий экземпляр «Snippet», учитывая проверенные данные
        :param instance:
        :param validated_data:
        :return:
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()

        return instance
