from django.db import models

class RockaePackageCatalogue(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the AI package or tool")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the AI package's functionality")
    repository_url = models.URLField(max_length=500, unique=True, help_text="URL to the package's repository")
    ai_category = models.CharField(max_length=100, help_text="Category of AI functionality (e.g., NLP, Computer Vision, Generation)")
    integration_type = models.CharField(max_length=100, help_text="Type of integration with Rockae (API, Library, Plugin)")
    supported_models = models.TextField(blank=True, null=True, help_text="List of supported AI models and versions")
    popularity_score = models.IntegerField(default=0, help_text="A score representing the package's popularity in AI applications")
    performance_metrics = models.JSONField(null=True, blank=True, help_text="Performance benchmarks and metrics")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-popularity_score']
        verbose_name = 'Open Source Package'
        verbose_name_plural = 'Open Source Packages'