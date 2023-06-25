from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


# abstract model class


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name=" Updated Date",
    )

    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date",
    )

    class Meta:
        abstract = True


# -------- abstract model ends -------


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
    )
    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text="This is variable of the setting.",
    )
    parameter = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Parameter",
    )

    def __str__(self):
        return f"general Setting: {self.name}"

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ("name",)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Name",
    )

    description = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Description",
        help_text="This is variable of the setting.",
    )

    file = models.ImageField(
        default="",
        verbose_name="Image",
        help_text="",
        blank=True,
        upload_to="Images/",
    )

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"
        ordering = ("name",)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name="Order",
    )
    backendname = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="backend name",
    )
    frontname = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="front name",
    )
    pmname = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="pm name",
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name="Percentage",
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    percentage3 = models.IntegerField(
        default=50,
        verbose_name="Percentage3",
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    percentage4 = models.IntegerField(
        default=50,
        verbose_name="Percentage4",
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f"Skills: {self.backendname},{self.frontname},{self.pmname}"

    class Meta:
        verbose_name = "Field"
        verbose_name_plural = "Fields"
        ordering = ("order",)


class Experiences(AbstractModel):
    company_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Company Name",
    )
    job_title = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Job Title",
    )
    job_location = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Job Location",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        verbose_name="End Date",
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return f"Experience: {self.company_name}"

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"


class Educations(AbstractModel):
    uni_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Uni Name",
    )
    edu_title = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Edu Title",
    )
    edu_location = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="Edu Location",
    )
    edustart_date = models.DateField(
        verbose_name="Start Date",
    )
    eduend_date = models.DateField(
        verbose_name="End Date",
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return f"Educations: {self.uni_name}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"


class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )

    slug = models.SlugField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Slug',
        help_text='',
    )

    button_text = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="button text",
        help_text="",
    )

    file = models.FileField(
        default="",
        verbose_name="File",
        help_text="",
        blank=True,
        upload_to="documents/",
    )

    def __str__(self):
        return f"Document: {self.slug}"

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ('order',)
    