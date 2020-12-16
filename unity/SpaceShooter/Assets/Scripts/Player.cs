using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    [SerializeField]
    private int moveSpeed = 10;
    [SerializeField]
    private GameObject projectilePrefab;
    [SerializeField]
    private int projectileSpeed = 1000;
    [SerializeField]
    private float fireRate = 0.5f;

    float xMin;
    float xMax;
    float yMin;
    float yMax;
        

    void Start()
    {
        SetUpGameBoundaries();
    }
    
    void Update()
    {
        Move();
        FireCoroutine();
    }

    void Move()
    {
        float deltaX = Input.GetAxis("Horizontal") * Time.deltaTime * moveSpeed;
        float newXPos = transform.position.x + deltaX;
        newXPos = Mathf.Clamp(newXPos, xMin, xMax);

        float deltaY = Input.GetAxis("Vertical") * Time.deltaTime * moveSpeed;
        float newYPos = transform.position.y + deltaY;
        newYPos = Mathf.Clamp(newYPos, yMin, yMax);

        transform.position = new Vector2(newXPos, newYPos);
    }

    IEnumerator Fire()
    {
        while (true)
        {
            GameObject laser = Instantiate(projectilePrefab, transform.position, Quaternion.identity) as GameObject;
            laser.GetComponent<Rigidbody2D>().velocity = new Vector2(0, projectileSpeed * Time.deltaTime);

            yield return new WaitForSeconds(fireRate);
        }
        
    }

    void FireCoroutine()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            StartCoroutine("Fire");
        }
        if (Input.GetButtonUp("Fire1"))
        {
            StopCoroutine("Fire");
        }
    }

    void SetUpGameBoundaries()
    {
        Camera gameCamera = Camera.main;

        xMin = gameCamera.ViewportToWorldPoint(new Vector3(.07f, 0, 0)).x;
        xMax = gameCamera.ViewportToWorldPoint(new Vector3(.93f, 0, 0)).x;
        yMin = gameCamera.ViewportToWorldPoint(new Vector3(0, .03f, 0)).y;
        yMax = gameCamera.ViewportToWorldPoint(new Vector3(0, .35f, 0)).y;
    }
}
